# ==========================================================
# FILE: preprocessing.py
#
# PURPOSE
# ----------------------------------------------------------
# Performs preprocessing on the FIFA World Cup dataset.
#
# Responsibilities:
#
# • Load the raw dataset
# • Handle missing values
# • Remove duplicate records
# • Standardize column names
# • Convert data types
# • Save the cleaned dataset
#
# The cleaned dataset is stored in:
#
#     data/processed/cleaned_world_cup_matches.csv
#
# Students should learn:
#
# ✓ Data cleaning workflow
# ✓ Pandas preprocessing
# ✓ Reusable preprocessing functions
# ✓ Saving processed datasets
#
# ==========================================================

import os
import pandas as pd

from config import Config


# ==========================================================
# Function: load_raw_data
# ==========================================================

def load_raw_data():
    """
    Load the raw World Cup dataset.

    Returns
    -------
    pandas.DataFrame
    """

    if not os.path.exists(Config.RAW_DATA_FILE):
        raise FileNotFoundError(
            f"Raw dataset not found:\n{Config.RAW_DATA_FILE}"
        )

    return pd.read_csv(Config.RAW_DATA_FILE)


# ==========================================================
# Function: clean_dataset
# ==========================================================

def clean_dataset(df):
    """
    Perform basic preprocessing.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    # ------------------------------------------------------
    # Standardize column names
    # ------------------------------------------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # ------------------------------------------------------
    # Remove duplicate rows
    # ------------------------------------------------------

    df = df.drop_duplicates()

    # ------------------------------------------------------
    # Remove rows with missing Year
    # ------------------------------------------------------

    df = df.dropna(subset=["year"])

    # ------------------------------------------------------
    # Convert year to integer
    # ------------------------------------------------------

    df["year"] = df["year"].astype(int)

    return df


# ==========================================================
# Function: save_processed_data
# ==========================================================

def save_processed_data(df):
    """
    Save cleaned dataset.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    str
        Output file path.
    """

    df.to_csv(
        Config.CLEANED_DATA_FILE,
        index=False
    )

    return Config.CLEANED_DATA_FILE


# ==========================================================
# Function: preprocess_worldcup_data
# ==========================================================

def preprocess_worldcup_data():
    """
    Complete preprocessing pipeline.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    df = load_raw_data()

    df = clean_dataset(df)

    save_processed_data(df)

    return df


# ==========================================================
# Function: preprocessing_summary
# ==========================================================

def preprocessing_summary():
    """
    Generate a preprocessing summary.

    Returns
    -------
    dict
    """

    df = preprocess_worldcup_data()

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum())
    }