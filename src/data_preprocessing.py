"""
Data preprocessing utilities for the transaction detection and risk monitoring project.

This module contains functions to load the raw SAML D dataset, clean missing
values, convert columns to appropriate data types, and perform any initial
transformations necessary before feature engineering.

Example usage:

    from src.data_preprocessing import load_raw_data, clean_data

    df_raw = load_raw_data("data/raw/SAML-D_reduced.txt")
    df_clean = clean_data(df_raw)

"""

from __future__ import annotations

import pandas as pd
from typing import Union


def load_raw_data(path: str, sep: str = ",", encoding: str = "utf-8") -> pd.DataFrame:
    """Load the raw transaction dataset from a CSV or TXT file.

    Args:
        path: Path to the raw data file.
        sep: Column delimiter (default is comma).
        encoding: File encoding.

    Returns:
        A pandas DataFrame containing the raw transactions.
    """
    return pd.read_csv(path, sep=sep, encoding=encoding)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data cleaning operations on the raw dataset.

    This function handles missing values, trims whitespace, and ensures that
    numeric columns are cast to appropriate types.

    Args:
        df: DataFrame containing the raw data.

    Returns:
        A cleaned DataFrame.
    """
    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # Convert numeric columns to floats where possible
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                continue

    # Drop rows with all missing values
    df = df.dropna(how="all")

    # Fill remaining missing values with column means for numeric columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mean())

    return df
