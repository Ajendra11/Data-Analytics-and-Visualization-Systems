# ==========================================================
# FILE: config.py
#
# PURPOSE
# ----------------------------------------------------------
# Central configuration for the Mini Sports Analytics
# Dashboard.
#
# This file stores:
#
# • Flask configuration
# • Project directory paths
# • Dataset locations
# • Visualization output paths
#
# Students should learn:
#
# ✓ Centralized configuration
# ✓ Absolute path management
# ✓ Separation of configuration from application logic
#
# ==========================================================

import os


class Config:
    """
    Application configuration.
    """

    # ======================================================
    # Flask Configuration
    # ======================================================

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key"
    )

    PROJECT_NAME = "Mini Sports Analytics Dashboard"

    # ======================================================
    # Project Root Directory
    #
    # This gives the absolute path to the project folder.
    #
    # Example:
    #
    # D:/mini-sports-analytics-web-app/
    # ======================================================

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    # ======================================================
    # Data Directories
    # ======================================================

    DATA_FOLDER = os.path.join(
        BASE_DIR,
        "data"
    )

    RAW_DATA_FOLDER = os.path.join(
        DATA_FOLDER,
        "raw"
    )

    PROCESSED_DATA_FOLDER = os.path.join(
        DATA_FOLDER,
        "processed"
    )

    # ======================================================
    # Static Directories
    # ======================================================

    STATIC_FOLDER = os.path.join(
        BASE_DIR,
        "static"
    )

    IMAGE_FOLDER = os.path.join(
        STATIC_FOLDER,
        "images"
    )

    PLOT_FOLDER = os.path.join(
        IMAGE_FOLDER,
        "plots"
    )

    # ======================================================
    # Visualization Output
    # ======================================================

    VISUALIZATION_OUTPUT_FOLDER = PLOT_FOLDER

    # ======================================================
    # Dataset Files
    # ======================================================

    RAW_DATA_FILE = os.path.join(
        RAW_DATA_FOLDER,
        "matches.csv"
    )

    CLEANED_DATA_FILE = os.path.join(
        PROCESSED_DATA_FOLDER,
        "cleaned_worldcup_matches.csv"
    )

    # ======================================================
    # Create Required Directories
    # ======================================================

    @staticmethod
    def create_directories():
        """
        Create required project directories if they do not
        already exist.
        """

        directories = [
            Config.DATA_FOLDER,
            Config.RAW_DATA_FOLDER,
            Config.PROCESSED_DATA_FOLDER,
            Config.STATIC_FOLDER,
            Config.IMAGE_FOLDER,
            Config.PLOT_FOLDER,
        ]

        for directory in directories:
            os.makedirs(
                directory,
                exist_ok=True
            )