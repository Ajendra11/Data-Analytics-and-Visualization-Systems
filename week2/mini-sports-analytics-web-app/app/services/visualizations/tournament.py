# ==========================================================
# FILE: tournament.py
#
# PURPOSE
# ----------------------------------------------------------
# Tournament-related visualizations for the FIFA World Cup
# dataset.
#
# This module contains plots that illustrate how the
# tournament has evolved over time.
#
# Visualizations
#
# • Matches per Tournament
# • Matches per Decade
#
# ==========================================================

from .helper import (
    setup_plot_style,
    load_processed_data,
    create_figure,
    save_plot,
)


# ==========================================================
# Plot: Matches per Tournament
# ==========================================================

def plot_matches_per_year():
    """
    Generate a line chart showing the number of
    matches played in each World Cup tournament.

    Returns
    -------
    dict
        Metadata describing the generated plot.
    """

    setup_plot_style()

    df = load_processed_data()

    matches = (
        df.groupby("year")
          .size()
          .sort_index()
    )

    fig, ax = create_figure()

    ax.plot(
        matches.index,
        matches.values,
        marker="o",
        linewidth=2,
        markersize=8
    )

    ax.set_title(
        "Matches Played by Tournament Year",
        fontsize=16
    )

    ax.set_xlabel("World Cup Year")

    ax.set_ylabel("Number of Matches")

    ax.grid(True, alpha=0.3)

    return save_plot(
        fig=fig,
        filename="matches_per_year.png",
        title="Matches Played by Tournament Year",
        caption=(
            "This line chart shows how the number of matches "
            "played in each FIFA World Cup has increased as "
            "the tournament expanded over time."
        )
    )


# ==========================================================
# Plot: Matches per Decade
# ==========================================================

def plot_matches_per_decade():
    """
    Generate a bar chart showing the total number
    of matches played in each decade.

    Returns
    -------
    dict
        Metadata describing the generated plot.
    """

    setup_plot_style()

    df = load_processed_data()

    decade = (df["year"] // 10) * 10

    matches = (
        decade.value_counts()
              .sort_index()
    )

    fig, ax = create_figure()

    ax.bar(
        matches.index.astype(str),
        matches.values
    )

    ax.set_title(
        "World Cup Matches by Decade",
        fontsize=16
    )

    ax.set_xlabel("Decade")

    ax.set_ylabel("Number of Matches")

    ax.grid(axis="y", alpha=0.3)

    return save_plot(
        fig=fig,
        filename="matches_per_decade.png",
        title="World Cup Matches by Decade",
        caption=(
            "This bar chart compares the total number of FIFA "
            "World Cup matches played during each decade, "
            "highlighting the long-term growth of the competition."
        )
    )