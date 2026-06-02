"""
Model training routines for the Transaction Detection & Risk Monitoring project.

This module defines a set of helper functions to load the cleaned transaction
data, engineer features, handle class imbalance, train multiple models, evaluate
them using common classification metrics, and persist the results for
subsequent reporting.  The focus is on reproducibility: all file operations
use :class:`pathlib.Path` and relative paths, and random seeds are exposed as
parameters.
"""

from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Tuple

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib


@dataclass
class TrainingResult:
    """Container for model training results."""
    name: str
    model_path: Path
    metrics: Dict[str, float]


def load_clean_data(path: Path) -> pd.DataFrame:
    """Load the cleaned dataset from disk.

    Parameters
    ----------
    path: pathlib.Path
        Path to the cleaned CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.
    """
    return pd.read_csv(path)


def prepare_dataset(
    df: pd.DataFrame,
    target_col: str,
    *,
    test_size: float = 0.3,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, ColumnTransformer]:
    """Split the DataFrame into training and testing sets and build a preprocessing pipeline.

    The function identifies numeric and categorical predictors, constructs a
    :class:`sklearn.compose.ColumnTransformer` that standardises numeric features and
    one‑hot encodes categorical ones, applies SMOTE to balance the classes, and
    returns transformed training and testing arrays along with the fitted
    transformer.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing features and target.
    target_col: str
        Name of the target column (binary indicator of suspicious activity).
    test_size: float, optional
        Proportion of the dataset to include in the test split.  Default is 0.3.
    random_state: int, optional
        Seed used by the random number generator.

    Returns
    -------
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    preprocessor: ColumnTransformer
    """
    df = df.copy()
    # Drop rows with missing target
    df = df.dropna(subset=[target_col])

    y = df[target_col]
    X = df.drop(columns=[target_col])

    numeric_cols = X.select_dtypes(include=['int64','float64']).columns.tolist()
    categorical_cols = X.select_dtypes(include=['object','category']).columns.tolist()

    # Remove potential target leakage columns
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ]
    )

    # Apply SMOTE after splitting to avoid data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # Fit preprocessor on training data
    X_train_pre = preprocessor.fit_transform(X_train)
    X_test_pre = preprocessor.transform(X_test)

    # Balance classes using SMOTE
    smote = SMOTE(random_state=random_state)
    X_train_bal, y_train_bal = smote.fit_resample(X_train_pre, y_train)

    return X_train_bal, X_test_pre, y_train_bal, y_test.values, preprocessor


def evaluate_model(model, X_test: np.ndarray, y_test: np.ndarray) -> Dict[str, float]:
    """Compute standard classification metrics for a fitted model."""
    y_pred = model.predict(X_test)
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1': f1_score(y_test, y_pred),
    }
    # Compute ROC‑AUC if probabilities are available
    if hasattr(model, 'predict_proba'):
        y_prob = model.predict_proba(X_test)[:, 1]
        metrics['ROC_AUC'] = roc_auc_score(y_test, y_prob)
    return metrics


def train_and_evaluate_models(
    cleaned_data_path: Path,
    target_col: str = 'is_laundering',
    models_dir: Path = Path('models'),
    *,
    random_state: int = 42,
) -> pd.DataFrame:
    """Train multiple models on the cleaned data and save their performance metrics.

    Two algorithms are trained by default: Logistic Regression and Random Forest.
    Additional algorithms can be added to the `models` dictionary.  Each model
    is persisted to disk using Joblib, and a comparison table is saved as
    `model_comparison.csv`.  A markdown file summarising the metrics is also
    generated.

    Parameters
    ----------
    cleaned_data_path: pathlib.Path
        Path to the cleaned CSV produced by the ETL notebook or preprocessing script.
    target_col: str, optional
        Name of the binary target column.  Default is 'is_laundering'.
    models_dir: pathlib.Path, optional
        Directory in which to save models and metrics.  Default is 'models'.
    random_state: int, optional
        Seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        DataFrame containing evaluation metrics for each model.
    """
    df = load_clean_data(cleaned_data_path)
    X_train, X_test, y_train, y_test, preprocessor = prepare_dataset(
        df, target_col, random_state=random_state
    )

    models_dir.mkdir(parents=True, exist_ok=True)

    # Define models to train
    model_specs = {
        'Logistic Regression': LogisticRegression(max_iter=1000, class_weight='balanced', random_state=random_state),
        'Random Forest': RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=random_state),
    }

    results = []
    for name, model in model_specs.items():
        # Fit model
        model.fit(X_train, y_train)
        # Evaluate
        metrics = evaluate_model(model, X_test, y_test)
        metrics['Model'] = name
        results.append(metrics)
        # Persist model
        model_path = models_dir / f"{name.lower().replace(' ', '_')}.joblib"
        joblib.dump(model, model_path)

    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    # Reorder columns
    cols = ['Model','Accuracy','Precision','Recall','F1'] + (['ROC_AUC'] if 'ROC_AUC' in results_df.columns else [])
    results_df = results_df[cols]

    # Save comparison CSV
    comparison_csv = models_dir / 'model_comparison.csv'
    results_df.to_csv(comparison_csv, index=False)

    # Save markdown metrics
    metrics_md_path = models_dir / 'model_metrics.md'
    with open(metrics_md_path, 'w') as f:
        f.write('# Model Evaluation Metrics\n\n')
        f.write(results_df.to_markdown(index=False))

    return results_df