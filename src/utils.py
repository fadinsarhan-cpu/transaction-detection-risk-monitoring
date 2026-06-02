"""
Utility functions for the transaction detection project.

This module contains helper functions that are used across multiple scripts,
such as saving models, logging results, or splitting datasets.  Keeping
utilities in a single place promotes code reuse and makes unit testing
easier.
"""

import os
import joblib
from typing import Any


def ensure_dir(path: str) -> None:
    """Ensure that a directory exists; create it if necessary."""
    os.makedirs(path, exist_ok=True)


def save_model(model: Any, path: str) -> None:
    """Serialise a trained model to disk using joblib.

    Args:
        model: Trained scikit‑learn estimator.
        path: Destination file path.
    """
    ensure_dir(os.path.dirname(path))
    joblib.dump(model, path)


def load_model(path: str) -> Any:
    """Load a model from disk.

    Args:
        path: Path to the serialised model file.

    Returns:
        The deserialised model.
    """
    return joblib.load(path)
