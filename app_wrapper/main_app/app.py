import importlib
import logging
import logging.config

#TODO  COMMENTED OUT IMPORTS WILL BE ADDED LATER ON
from flask import Flask
# from flask_cors import CORS

# from . import commands, users
from . import main, commands
from .main_service import views as main_app_views
from .tests.views import test_blueprint
from .config import ALLOWED_ORIGINS, DEBUG, ENV
from .extensions import api, db, migrate

# from .loggers.logger_config import LOGGER_DEV_CONFIG, LOGGER_PRODUCTION_CONFIG
# from .tests.views import test_blueprint

# from .commons.error_handle import register_error_handlers


logger = logging.getLogger(__name__)


def create_app(config_object="app_wrapper.config"):

    """Application factory, used to create application"""
    app = Flask(
        "ml_app",
    )

    app.config.from_object(config_object)

    # propagate to pass 500
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # stop enforcing / at the end of urls
    app.url_map.strict_slashes = False


    configure_extensions(app)
    configure_cognito(app)
    register_blueprints(app)
    register_namespaces(app)
    # CORS(app, origins=ALLOWED_ORIGINS)

    register_commands(app)
    # register_error_handlers(app)
    return app





def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)



def configure_cognito(app):
    importlib.import_module("locations_api.auth.identity_handler")


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(main.views.blueprint)
    if DEBUG or app.testing:
        app.register_blueprint(test_blueprint)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.initdb)

def register_namespaces(app):
    api.add_namespace(main_app_views.ns)
