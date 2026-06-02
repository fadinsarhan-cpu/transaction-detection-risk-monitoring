"""
Data preprocessing utilities for the Transaction Detection & Risk Monitoring project.

This module encapsulates all of the logic required to ingest the raw SAML‑D
transaction dataset, clean and standardise it, engineer a few simple risk
features, and persist the result to the `data/processed/` folder.  All file
interactions use :class:`pathlib.Path` objects rather than hard‑coded
strings to ensure reproducibility across operating systems.  Typical usage
looks like this:

    from pathlib import Path
    from src.data_preprocessing import load_raw_data, clean_data,
        add_basic_risk_features, save_cleaned_data

    raw_df = load_raw_data(Path('data/raw') / 'SAML-D_reduced.txt')
    cleaned_df = clean_data(raw_df)
    enriched_df = add_basic_risk_features(cleaned_df)
    save_cleaned_data(enriched_df, Path('data/processed') / 'cleaned_transactions.csv')

"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable
import pandas as pd


def load_raw_data(path: Path, *, sep: str = ',', encoding: str = 'utf-8', **read_kwargs) -> pd.DataFrame:
    """Load the raw transaction dataset from a CSV or TXT file.

    Parameters
    ----------
    path: pathlib.Path
        The path to the raw data file.  Using a Path instead of a plain string
        helps avoid issues with operating system separators.
    sep: str, optional
        The column delimiter.  Default is a comma.  Adjust if your raw
        dataset uses a different delimiter (e.g., tab or pipe).
    encoding: str, optional
        The file encoding to use when reading text.
    **read_kwargs:
        Additional keyword arguments passed directly to :func:`pandas.read_csv`.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the raw transactions.
    """
    return pd.read_csv(path, sep=sep, encoding=encoding, **read_kwargs)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data cleaning operations on a DataFrame.

    The cleaning steps include:

    * Standardising column names to lowercase with underscores
    * Stripping whitespace from string values
    * Converting string‑based numeric fields where possible
    * Dropping rows that are completely empty
    * Filling remaining missing values in numeric columns with the column mean
    * Removing duplicate rows

    Parameters
    ----------
    df: pd.DataFrame
        Raw transaction data.

    Returns
    -------
    pd.DataFrame
        Cleaned dataset ready for feature engineering.
    """
    # Standardise column names
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )

    # Strip whitespace from object/string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # Attempt to convert object columns to numeric where appropriate
    for col in df.columns:
        if df[col].dtype == object:
            new_col = pd.to_numeric(df[col], errors='ignore')
            # Only replace if at least some values converted
            if not new_col.equals(df[col]):
                df[col] = new_col

    # Drop rows that are entirely missing
    df = df.dropna(how='all')

    # Fill missing numeric values with column mean
    for col in df.select_dtypes(include=['int64','float64']).columns:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mean())

    # Remove duplicate rows
    df = df.drop_duplicates()
    return df


def add_basic_risk_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple risk‑related features to the dataset.

    This helper creates basic fields that may be useful for downstream analyses
    and modelling, such as transaction amount bands and large transaction flags.

    Parameters
    ----------
    df: pd.DataFrame
        Cleaned transaction data containing at least an ``amount`` column.

    Returns
    -------
    pd.DataFrame
        DataFrame with additional risk feature columns.
    """
    df = df.copy()
    if 'amount' in df.columns:
        # Create quartile‑based amount bands
        df['amount_band'] = pd.qcut(df['amount'], q=4, labels=['low','medium','high','very_high'])
        # Flag very large transactions (top 5%)
        threshold = df['amount'].quantile(0.95)
        df['large_transaction_flag'] = (df['amount'] > threshold).astype(int)

    # Add sender risk ratio if the label exists
    if {'sender_account','is_laundering'}.issubset(df.columns):
        ratio = df.groupby('sender_account')['is_laundering'].mean()
        df['sender_risk_ratio'] = df['sender_account'].map(ratio)

    return df


def save_cleaned_data(df: pd.DataFrame, output_path: Path) -> None:
    """Persist the cleaned and enriched dataset to disk.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame to save.
    output_path: pathlib.Path
        Destination CSV path.  The parent directory will be created if it does
        not already exist.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def preprocess_and_save(
    raw_path: Path,
    processed_path: Path,
    *,
    sep: str = ',',
    encoding: str = 'utf-8',
    read_kwargs: dict | None = None,
) -> pd.DataFrame:
    """End‑to‑end convenience function to load, clean, enrich and save data.

    This helper orchestrates the typical workflow: read the raw file, perform
    cleaning, add risk features and write the result to the processed
    location.

    Parameters
    ----------
    raw_path: pathlib.Path
        Path to the raw data file.
    processed_path: pathlib.Path
        Output path for the cleaned dataset.
    sep: str
        Field delimiter passed to :func:`pandas.read_csv`.
    encoding: str
        Text encoding for the raw file.
    read_kwargs: dict, optional
        Additional arguments for :func:`pandas.read_csv`.

    Returns
    -------
    pd.DataFrame
        The cleaned and enriched DataFrame.
    """
    read_kwargs = read_kwargs or {}
    df_raw = load_raw_data(raw_path, sep=sep, encoding=encoding, **read_kwargs)
    df_clean = clean_data(df_raw)
    df_enriched = add_basic_risk_features(df_clean)
    save_cleaned_data(df_enriched, processed_path)
    return df_enriched
