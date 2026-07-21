# ==========================================================
# FILE: test_visualizations.py
#
# PURPOSE
# ----------------------------------------------------------
# Test all visualization modules.
#
# This script verifies that visualization functions:
#
# • Execute successfully
# • Save image files
# • Return metadata
#
# ==========================================================

import os
import sys

# ==========================================================
# Add Project Root to Python Path
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Imports
# ==========================================================

from config import Config

# Create required directories
Config.create_directories()

from app.services.visualizations.tournament import (
    plot_matches_per_year,
    plot_matches_per_decade,
)

from app.services.visualizations.geography import (
    plot_top_host_cities,
    plot_top_stadiums,
)

# ==========================================================
# Helper Function
# ==========================================================

def verify_plot(plot_info):
    """
    Verify that a visualization has been created.
    """

    image_path = os.path.join(
        Config.VISUALIZATION_OUTPUT_FOLDER,
        plot_info["filename"]
    )

    print("\n----------------------------------------")
    print(f"Title    : {plot_info['title']}")
    print(f"Filename : {plot_info['filename']}")

    if os.path.exists(image_path):
        print("✓ Image successfully created")
    else:
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    print(f"Caption  : {plot_info['caption']}")


# ==========================================================
# Tournament Visualizations
# ==========================================================

def test_tournament_visualizations():

    print("\nGenerating Tournament Visualizations...")

    verify_plot(
        plot_matches_per_year()
    )

    verify_plot(
        plot_matches_per_decade()
    )


# ==========================================================
# Geography Visualizations
# ==========================================================

def test_geography_visualizations():

    print("\nGenerating Geography Visualizations...")

    verify_plot(
        plot_top_host_cities()
    )

    verify_plot(
        plot_top_stadiums()
    )


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("TESTING VISUALIZATION MODULE")
    print("=" * 60)

    try:

        test_tournament_visualizations()

        test_geography_visualizations()

        print("\n" + "=" * 60)
        print("ALL VISUALIZATION TESTS PASSED")
        print("=" * 60)

    except Exception as e:

        print("\n❌ TEST FAILED")
        print(e)


if __name__ == "__main__":
    main()