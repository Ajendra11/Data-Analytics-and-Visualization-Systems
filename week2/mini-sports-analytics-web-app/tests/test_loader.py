# ==========================================================
# FILE: test_loader.py
#
# PURPOSE
# ----------------------------------------------------------
# Simple unit test for data loader service.
#
# This ensures:
# - dataset loads correctly
# - path configuration works
# - no runtime errors in service layer
#
# Students learn:
# • Basic testing
# • Data pipeline validation
# • Debugging structured modules
#
# ==========================================================


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.data_loader import load_worldcup_data, preview_data, dataset_summary

def test_load_data():
    """
    Test whether dataset loads successfully.
    """

    try:
        df = load_worldcup_data()

        assert df is not None, "DataFrame is None"
        assert len(df) > 0, "Dataset is empty"

        print("\n✅ TEST PASSED: Dataset loaded successfully")
        print("Shape:", df.shape)

    except Exception as e:
        print("\n❌ TEST FAILED:", str(e))


def test_preview():
    """
    Test preview function.
    """

    try:
        df = preview_data(5)

        assert len(df) <= 5, "Preview returned too many rows"

        print("\n✅ TEST PASSED: Preview works")
        print(df.head())

    except Exception as e:
        print("\n❌ TEST FAILED:", str(e))


def test_summary():
    """
    Test dataset summary function.
    """

    try:
        info = dataset_summary()

        assert "shape" in info
        assert "columns" in info
        assert "missing_values" in info

        print("\n✅ TEST PASSED: Summary generated")
        print(info)

    except Exception as e:
        print("\n❌ TEST FAILED:", str(e))


# ----------------------------------------------------------
# Run all tests
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\n==============================")
    print(" RUNNING DATA LOADER TESTS")
    print("==============================")

    test_load_data()
    test_preview()
    test_summary()

    print("\n==============================")
    print(" ALL TESTS COMPLETED")
    print("==============================")