# ==========================================================
# FILE: data_loader.py
#
# PURPOSE
# ----------------------------------------------------------
# Centralized data loading service.
#
# This module provides reusable functions for loading and
# previewing the FIFA World Cup dataset. Dataset locations
# are managed through the application configuration to avoid
# hardcoding file paths throughout the project.
#
# Students should learn:
# • Centralized data loading
# • Configuration-driven file management
# • Reusable service modules
#
# ==========================================================

import os
import pandas as pd

from config import Config


# ==========================================================
# Function: load_worldcup_data
# ==========================================================

def load_worldcup_data():
    """
    Load the raw FIFA World Cup dataset.

    Returns
    -------
    pandas.DataFrame
        Raw World Cup dataset.
    """

    if not os.path.exists(Config.RAW_DATA_FILE):
        raise FileNotFoundError(
            f"Dataset not found:\n{Config.RAW_DATA_FILE}"
        )

    return pd.read_csv(Config.RAW_DATA_FILE)


# ==========================================================
# Function: preview_data
# ==========================================================

def preview_data(n=5):
    """
    Display the first n rows of the dataset.

    Parameters
    ----------
    n : int, default=5

    Returns
    -------
    pandas.DataFrame
    """

    df = load_worldcup_data()

    return df.head(n)


# ==========================================================
# Function: dataset_summary
# ==========================================================

def dataset_summary():
    """
    Generate a high-level summary of the dataset.

    Returns
    -------
    dict
        Dictionary containing:

        - Shape
        - Columns
        - Data types
        - Missing values
    """

    df = load_worldcup_data()

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }