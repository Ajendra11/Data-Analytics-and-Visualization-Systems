# ==========================================================
# FILE: geography.py
#
# PURPOSE
# ----------------------------------------------------------
# Visualization module for geographical insights.
#
# This module generates visualizations related to where
# FIFA World Cup matches have been played.
#
# Visualizations
#
# 1. Top Host Cities
# 2. Top Stadiums
#
# ==========================================================

from .helper import (
    setup_plot_style,
    load_processed_data,
    create_figure,
    save_plot
)


# ==========================================================
# Plot: Top Host Cities
# ==========================================================

def plot_top_host_cities(top_n=10):
    """
    Generate a horizontal bar chart showing the cities
    that have hosted the most FIFA World Cup matches.

    Parameters
    ----------
    top_n : int
        Number of cities to display.

    Returns
    -------
    dict
        Plot metadata.
    """

    setup_plot_style()

    df = load_processed_data()

    city_counts = (
        df["city"]
        .value_counts()
        .head(top_n)
        .sort_values()
    )

    fig, ax = create_figure(figsize=(10, 7))

    ax.barh(
        city_counts.index,
        city_counts.values
    )

    ax.set_title(
        f"Top {top_n} Host Cities"
    )

    ax.set_xlabel(
        "Number of Matches"
    )

    ax.set_ylabel(
        "City"
    )

    ax.grid(
        axis="x",
        alpha=0.3
    )

    return save_plot(

        fig=fig,

        filename="top_host_cities.png",

        title="Top Host Cities",

        caption=(
            "Displays the cities that have hosted the greatest "
            "number of FIFA World Cup matches throughout the "
            "history of the tournament."
        )

    )


# ==========================================================
# Plot: Top Stadiums
# ==========================================================

def plot_top_stadiums(top_n=10):
    """
    Generate a horizontal bar chart showing the stadiums
    that have hosted the most FIFA World Cup matches.

    Parameters
    ----------
    top_n : int
        Number of stadiums to display.

    Returns
    -------
    dict
        Plot metadata.
    """

    setup_plot_style()

    df = load_processed_data()

    stadium_counts = (
        df["stadium"]
        .value_counts()
        .head(top_n)
        .sort_values()
    )

    fig, ax = create_figure(figsize=(10, 7))

    ax.barh(
        stadium_counts.index,
        stadium_counts.values
    )

    ax.set_title(
        f"Top {top_n} World Cup Stadiums"
    )

    ax.set_xlabel(
        "Number of Matches"
    )

    ax.set_ylabel(
        "Stadium"
    )

    ax.grid(
        axis="x",
        alpha=0.3
    )

    return save_plot(

        fig=fig,

        filename="top_stadiums.png",

        title="Top World Cup Stadiums",

        caption=(
            "Shows the stadiums that have hosted the highest "
            "number of FIFA World Cup matches, highlighting "
            "iconic venues used repeatedly across tournaments."
        )

    )