# ==========================================================
# FILE: __init__.py
#
# PURPOSE
# ----------------------------------------------------------
# Initializes the Flask application.
#
# Responsibilities:
# • Create Flask application
# • Load configuration
# • Create required project directories
# • Register application blueprints
#
# ==========================================================

from flask import Flask
from config import Config


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    # ------------------------------------------------------
    # Load application configuration
    # ------------------------------------------------------

    app.config.from_object(Config)

    # ------------------------------------------------------
    # Ensure required directories exist
    # ------------------------------------------------------

    Config.create_directories()

    # ------------------------------------------------------
    # Register Blueprints
    # ------------------------------------------------------

    from app.routes import main
    app.register_blueprint(main)

    return app