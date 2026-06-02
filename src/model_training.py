import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

from .data_preprocessing import load_and_clean_data
from .feature_engineering import build_feature_pipeline


def train_and_evaluate(raw_data_path: str):
    """Train a risk classification model and evaluate it."""
    # Load and clean data
    data = load_and_clean_data(raw_data_path)

    # Identify target and features
    y = data["risk_flag"]
    X = data.drop(columns=["risk_flag"])

    # Prepare preprocessing pipeline for features
    pipeline, feature_names = build_feature_pipeline(X)

    # Fit the pipeline and transform features
    X_processed = pipeline.fit_transform(X)

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Compute evaluation metrics
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    metrics = {
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "roc_auc": roc_auc,
    }

    return model, metrics, feature_names
