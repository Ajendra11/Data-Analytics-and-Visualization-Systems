# ==========================================================
# FILE: app/services/statistics.py
#
# PURPOSE
# ----------------------------------------------------------
# Converts cleaned World Cup dataset into structured KPI
# metrics for dashboard consumption with dynamic year filtering.
#
# OUTPUT GROUPS:
#   1. tournament_kpis
#   2. venue_kpis
#   3. competition_kpis
#   4. team_kpis
#   5. temporal_kpis
#
# ==========================================================

import os
import pandas as pd
from config import Config

FILE_NAME = "cleaned_worldcup_matches.csv"


# ----------------------------------------------------------
# Load processed dataset
# ----------------------------------------------------------
def load_data():
    path = os.path.join(Config.PROCESSED_DATA_FOLDER, FILE_NAME)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed dataset not found at {path}")

    return pd.read_csv(path)


# ==========================================================
# 1. TOURNAMENT KPIs
# ==========================================================
def tournament_kpis(df=None):
    if df is None:
        df = load_data()

    if df.empty:
        return {
            "total_matches": 0,
            "total_teams": 0,
            "total_stadiums": 0,
            "total_cities": 0,
            "total_years": 0,
        }

    return {
        "total_matches": int(len(df)),
        "total_teams": int(
            len(set(df["home_team"]).union(set(df["away_team"])))
        ),
        "total_stadiums": int(df["stadium"].nunique()),
        "total_cities": int(df["city"].nunique()),
        "total_years": int(df["year"].nunique()),
    }


# ==========================================================
# 2. VENUE KPIs
# ==========================================================
def venue_kpis(df=None):
    if df is None:
        df = load_data()

    if df.empty:
        return {"top_stadiums": {}, "top_cities": {}}

    return {
        "top_stadiums": df["stadium"].value_counts().head(5).to_dict(),
        "top_cities": df["city"].value_counts().head(5).to_dict(),
    }


# ==========================================================
# 3. COMPETITION KPIs
# ==========================================================
def competition_kpis(df=None):
    if df is None:
        df = load_data()

    if df.empty:
        return {"stage_distribution": {}}

    stage_distribution = df["stage"].value_counts().to_dict()

    return {"stage_distribution": stage_distribution}


# ==========================================================
# 4. TEAM KPIs
# ==========================================================
def team_kpis(df=None):
    if df is None:
        df = load_data()

    if df.empty:
        return {"top_teams": {}, "team_participation_score": {}}

    teams = pd.concat([df["home_team"], df["away_team"]])

    # 1. Convert value_counts to DataFrame
    counts_df = teams.value_counts().reset_index()
    counts_df.columns = ["team", "count"]

    # 2. Sort strictly by count (Descending), then team name (Ascending) for ties
    counts_df = counts_df.sort_values(
        by=["count", "team"], ascending=[False, True]
    )

    # 3. Convert back to dictionaries maintaining sorted order
    top_teams_dict = dict(
        zip(
            counts_df["team"].head(10),
            counts_df["count"].head(10).astype(int),
        )
    )
    all_teams_dict = dict(
        zip(counts_df["team"], counts_df["count"].astype(int))
    )

    return {
        "top_teams": top_teams_dict,
        "team_participation_score": all_teams_dict,
    }


# ==========================================================
# 5. TEMPORAL KPIs
# ==========================================================
def temporal_kpis(df=None):
    if df is None:
        df = load_data()

    if df.empty:
        return {"matches_per_year": {}, "peak_year": 0, "peak_matches": 0}

    matches_per_year = df["year"].value_counts().sort_index()

    peak_year = (
        int(matches_per_year.idxmax()) if not matches_per_year.empty else 0
    )
    peak_value = (
        int(matches_per_year.max()) if not matches_per_year.empty else 0
    )

    return {
        "matches_per_year": matches_per_year.to_dict(),
        "peak_year": peak_year,
        "peak_matches": peak_value,
    }


# ==========================================================
# FULL KPI REPORT
# ==========================================================
def generate_kpi_report(df=None, year=None):
    """
    Generates full KPI dictionary.
    Supports optional year filtering.
    """
    if df is None:
        df = load_data()

    # Filter by selected year if provided
    if year is not None:
        df = df[df["year"] == year]

    return {
        "tournament_kpis": tournament_kpis(df),
        "venue_kpis": venue_kpis(df),
        "competition_kpis": competition_kpis(df),
        "team_kpis": team_kpis(df),
        "temporal_kpis": temporal_kpis(df),
    }