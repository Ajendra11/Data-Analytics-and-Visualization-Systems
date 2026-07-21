# ==========================================================
# FILE: test_eda.py
#
# PURPOSE
# ----------------------------------------------------------
# Test the Exploratory Data Analysis (EDA) module.
#
# ==========================================================

import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.services.eda import run_eda


# ==========================================================
# Test Complete EDA Pipeline
# ==========================================================

def test_run_eda():

    report = run_eda()

    assert isinstance(report, dict)

    required_sections = [
        "tournament_overview",
        "geography",
        "match_density",
        "team_participation",
        "time_based_insights"
    ]

    for section in required_sections:

        assert section in report, f"Missing section: {section}"

    print("\n========== EDA REPORT ==========\n")

    for section, content in report.items():

        print(section.upper())

        print("-" * 40)

        print(content)

        print()


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print(" TESTING EDA MODULE ")
    print("=" * 50)

    test_run_eda()

    print("=" * 50)
    print(" ALL EDA TESTS PASSED ")
    print("=" * 50)