# ==========================================================
# FILE: helper.py
#
# PURPOSE
# ----------------------------------------------------------
# Shared helper functions for all visualization modules.
#
# Responsibilities
#
# • Load processed dataset
# • Configure plotting style
# • Save figures
# • Return metadata for Flask templates
#
# ==========================================================

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import Config


# ==========================================================
# Configure Plot Style
# ==========================================================

def setup_plot_style():
    """
    Configure a consistent plotting style for all figures.
    """

    plt.style.use("ggplot")

    sns.set_theme(
        style="whitegrid",
        context="talk"
    )


# ==========================================================
# Load Processed Dataset
# ==========================================================

def load_processed_data():
    """
    Load the cleaned World Cup dataset.

    Returns
    -------
    pandas.DataFrame
    """

    if not os.path.exists(Config.CLEANED_DATA_FILE):

        raise FileNotFoundError(
            f"Processed dataset not found:\n"
            f"{Config.CLEANED_DATA_FILE}"
        )

    return pd.read_csv(
        Config.CLEANED_DATA_FILE
    )


# ==========================================================
# Save Plot
# ==========================================================

def save_plot(
    fig,
    filename,
    title,
    caption
):
    """
    Save a matplotlib figure and return its metadata.

    Parameters
    ----------
    fig : matplotlib.figure.Figure

    filename : str

    title : str

    caption : str

    Returns
    -------
    dict
    """

    output_path = os.path.join(
        Config.VISUALIZATION_OUTPUT_FOLDER,
        filename
    )

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    return {

        "title": title,

        "filename": filename,

        "caption": caption

    }


# ==========================================================
# Create Figure
# ==========================================================

def create_figure(
    figsize=(10, 6)
):
    """
    Create a standard matplotlib figure.

    Returns
    -------
    figure, axis
    """

    fig, ax = plt.subplots(
        figsize=figsize
    )

    return fig, ax