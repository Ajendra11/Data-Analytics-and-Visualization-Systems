# ==========================================================
# FILE: eda.py
#
# PURPOSE
# ----------------------------------------------------------
# Performs Exploratory Data Analysis (EDA) on the cleaned
# FIFA World Cup dataset.
#
# The goal of this module is to generate meaningful insights
# that help understand the tournament structure before
# building statistical models or visualizations.
#
# EDA MODULES
#
# 1. Tournament Overview
# 2. Geography of Football
# 3. Match Density Analysis
# 4. Team Participation
# 5. Time-based Insights
#
# Students should learn:
#
# ✓ Exploratory Data Analysis
# ✓ Data aggregation
# ✓ Frequency analysis
# ✓ Grouping operations
#
# ==========================================================

import os
import pandas as pd

from config import Config


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
            f"Processed dataset not found:\n{Config.CLEANED_DATA_FILE}"
        )

    return pd.read_csv(Config.CLEANED_DATA_FILE)


# ==========================================================
# 1. Tournament Overview
# ==========================================================

def tournament_overview():

    df = load_processed_data()

    return {
        "total_matches": len(df),
        "total_tournaments": df["year"].nunique(),
        "unique_stadiums": df["stadium"].nunique(),
        "unique_cities": df["city"].nunique()
    }


# ==========================================================
# 2. Geography of Football
# ==========================================================

def geography_analysis():

    df = load_processed_data()

    return {
        "top_cities": df["city"].value_counts().head(5).to_dict(),
        "top_stadiums": df["stadium"].value_counts().head(5).to_dict()
    }


# ==========================================================
# 3. Match Density Analysis
# ==========================================================

def match_density_analysis():

    df = load_processed_data()

    return {
        "matches_per_year": (
            df["year"]
            .value_counts()
            .sort_index()
            .to_dict()
        ),
        "matches_per_stage": (
            df["stage"]
            .value_counts()
            .to_dict()
        )
    }


# ==========================================================
# 4. Team Participation
# ==========================================================

def team_participation():

    df = load_processed_data()

    teams = pd.concat(
        [
            df["home_team_initials"],
            df["away_team_initials"]
        ]
    )

    appearances = teams.value_counts()

    return {
        "top_teams": appearances.head(10).to_dict(),
        "all_team_appearances": appearances.to_dict()
    }


# ==========================================================
# 5. Time-based Insights
# ==========================================================

def time_based_insights():

    df = load_processed_data()

    decade = (df["year"] // 10) * 10

    return {
        "matches_per_year": (
            df["year"]
            .value_counts()
            .sort_index()
            .to_dict()
        ),
        "matches_per_decade": (
            decade
            .value_counts()
            .sort_index()
            .to_dict()
        )
    }


# ==========================================================
# Run Complete EDA
# ==========================================================

def run_eda():

    return {
        "tournament_overview": tournament_overview(),
        "geography": geography_analysis(),
        "match_density": match_density_analysis(),
        "team_participation": team_participation(),
        "time_based_insights": time_based_insights()
    }