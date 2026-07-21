"""
Application Routes

This module defines the URL routes for the Mini Sports Analytics Web App.
Each route delegates data fetching/computation to the service layer 
and passes the data to the corresponding HTML template.
"""

from flask import Blueprint, jsonify, render_template, request

# 1. Import Service Layer Functions
from app.services.statistics import generate_kpi_report

# Try importing optional EDA and Visualization services if present
try:
    from app.services.data_loader import load_raw_data
    from app.services.eda import generate_summary
except ImportError:
    load_raw_data = None
    generate_summary = None

try:
    from app.visualizations.generate import generate_all_plots
except ImportError:
    generate_all_plots = None


# Create Blueprint
main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Home page / Main Dashboard overview."""
    try:
        report = generate_kpi_report()
    except Exception:
        report = {}
    return render_template("index.html", report=report)


@main.route("/preprocessing")
def preprocessing():
    """Data preprocessing page."""
    summary = None
    if load_raw_data and generate_summary:
        try:
            df_raw = load_raw_data()
            summary = generate_summary(df_raw)
        except Exception:
            summary = None

    return render_template("preprocessing.html", summary=summary)


@main.route("/eda")
def eda():
    """Exploratory Data Analysis (EDA) page with dynamic year filtering."""
    # 1. Read 'year' parameter from query string (e.g., /eda?year=2018)
    selected_year = request.args.get("year", type=int)

    # 2. Fetch report (filtered by year if provided)
    try:
        report = generate_kpi_report(year=selected_year)
    except TypeError:
        # Fallback if generate_kpi_report does not accept year parameter yet
        report = generate_kpi_report()
    except Exception:
        report = {}

    # 3. Available World Cup tournament years for the filter dropdown
    available_years = [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 
        1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 
        2010, 2014, 2018, 2022
    ]

    return render_template(
        "eda.html",
        report=report,
        selected_year=selected_year,
        available_years=available_years
    )


@main.route("/statistics")
def statistics():
    """Statistical analysis page."""
    try:
        report = generate_kpi_report()
    except Exception:
        report = {}

    return render_template("statistics.html", report=report)


@main.route("/visualizations")
def visualizations():
    """Data visualization page."""
    plots = []
    if generate_all_plots:
        try:
            plots = generate_all_plots()
        except Exception:
            plots = []

    return render_template("visualization.html", plots=plots)


@main.route("/about")
def about():
    """About the project page."""
    return render_template("about.html")


# ==========================================================
# STEP 4: REST API ENDPOINTS
# ==========================================================
@main.route("/api/kpis")
def api_kpis():
    """
    REST API endpoint returning structured KPI JSON data.
    Supports year filtering via query string: /api/kpis?year=2022
    """
    selected_year = request.args.get("year", type=int)

    try:
        report = generate_kpi_report(year=selected_year)
        return jsonify({
            "status": "success",
            "year": selected_year,
            "data": report
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500