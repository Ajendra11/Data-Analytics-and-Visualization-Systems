import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.statistics import generate_kpi_report


def test_statistics_engine():
    report = generate_kpi_report()

    # Top-level structure checks
    required_keys = [
        "tournament_kpis",
        "venue_kpis",
        "competition_kpis",
        "team_kpis",
        "temporal_kpis"
    ]

    for key in required_keys:
        assert key in report, f"Missing key: {key}"

    # Basic sanity checks
    assert report["tournament_kpis"]["total_matches"] > 0
    assert len(report["venue_kpis"]["top_stadiums"]) <= 5
    assert "matches_per_year" in report["temporal_kpis"]

    print("\n✅ STATISTICS ENGINE WORKING")
    print("\n--- SAMPLE OUTPUT ---")
    print(report)


if __name__ == "__main__":
    print("\n==============================")
    print(" RUNNING STATISTICS TESTS")
    print("==============================")

    test_statistics_engine()

    print("\n==============================")
    print(" ALL TESTS COMPLETED")
    print("==============================")