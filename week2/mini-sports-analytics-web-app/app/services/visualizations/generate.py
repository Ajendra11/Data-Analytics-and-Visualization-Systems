# ==========================================================
# FILE: generate.py
#
# PURPOSE
# ----------------------------------------------------------
# Generate all visualization assets used by the dashboard.
#
# This module acts as the integration layer between
# individual visualization modules and the Flask routes.
#
# ==========================================================

from .tournament import (
    plot_matches_per_year,
    plot_matches_per_decade,
)

from .geography import (
    plot_top_host_cities,
    plot_top_stadiums,
)


# ==========================================================
# Tournament Visualizations
# ==========================================================

def generate_tournament_visualizations():
    """
    Generate all tournament visualizations.

    Returns
    -------
    list
    """

    return [

        plot_matches_per_year(),

        plot_matches_per_decade()

    ]


# ==========================================================
# Geography Visualizations
# ==========================================================

def generate_geography_visualizations():
    """
    Generate all geography visualizations.

    Returns
    -------
    list
    """

    return [

        plot_top_host_cities(),

        plot_top_stadiums()

    ]


# ==========================================================
# Generate Everything
# ==========================================================

def generate_all_visualizations():
    """
    Generate every visualization required by the dashboard.

    Returns
    -------
    list
    """

    plots = []

    plots.extend(
        generate_tournament_visualizations()
    )

    plots.extend(
        generate_geography_visualizations()
    )

    return plots