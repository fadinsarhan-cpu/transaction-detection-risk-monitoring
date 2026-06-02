"""
Feature engineering functions for transaction detection.

This module defines operations to transform cleaned data into a set of
features suitable for machine learning models.  Feature engineering may
include one‑hot encoding of categorical variables, scaling of numeric
attributes, and generation of derived variables (e.g., transaction frequency
per account).
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from typing import Tuple


def build_feature_pipeline(df: pd.DataFrame) -> Tuple[Pipeline, list[str]]:
    """Build a scikit‑learn pipeline for feature engineering.

    Args:
        df: Cleaned DataFrame containing raw features.

    Returns:
        A tuple containing the fitted preprocessing pipeline and the list of
        feature names after transformation.
    """
    categorical_cols = df.select_dtypes(include="object").columns.tolist()
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    categorical_transformer = Pipeline(steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols),
        ]
    )

    # Fit the transformer to extract feature names
    preprocessor.fit(df)

    # Build feature names after one‑hot encoding
    feature_names = []
    if numeric_cols:
        feature_names.extend(numeric_cols)
    if categorical_cols:
        ohe = preprocessor.named_transformers_["cat"]["onehot"]
        ohe_features = ohe.get_feature_names_out(categorical_cols)
        feature_names.extend(ohe_features.tolist())

    return preprocessor, feature_names
