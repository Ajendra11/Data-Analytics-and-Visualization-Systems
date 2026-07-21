# ==========================================================
# FILE: test_preprocessing.py
#
# PURPOSE
# ----------------------------------------------------------
# Test the preprocessing pipeline.
#
# This script verifies that:
#
# • The raw dataset can be loaded.
# • The preprocessing pipeline executes successfully.
# • The cleaned dataset is saved.
# • The returned object is a DataFrame.
#
# ==========================================================

import os
import sys
import pandas as pd

# ----------------------------------------------------------
# Add project root to Python path
# ----------------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from config import Config
from app.services.preprocessing import (
    preprocess_worldcup_data,
    preprocessing_summary
)


# ==========================================================
# Test 1: Preprocessing Pipeline
# ==========================================================

def test_preprocessing_pipeline():

    print("\nRunning preprocessing pipeline...")

    df = preprocess_worldcup_data()

    assert isinstance(df, pd.DataFrame)

    assert len(df) > 0

    assert os.path.exists(
        Config.CLEANED_DATA_FILE
    )

    print("✅ Preprocessing completed successfully.")


# ==========================================================
# Test 2: Summary Report
# ==========================================================

def test_summary():

    summary = preprocessing_summary()

    print("\nDataset Summary")

    print("-" * 40)

    for key, value in summary.items():
        print(f"{key}:")
        print(value)
        print()


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print(" TESTING PREPROCESSING MODULE ")
    print("=" * 50)

    test_preprocessing_pipeline()

    test_summary()

    print("=" * 50)
    print(" ALL PREPROCESSING TESTS PASSED ")
    print("=" * 50)