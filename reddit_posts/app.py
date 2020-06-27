from flask import Flask
from . import connexion
from .ext import commands, scheduler, database, settings


def create_app(**config) -> Flask:
    """
    Create a Flask object app by connexion
    :return: Flask
    """
    app = connexion.app
    connexion.add_api('swagger.yaml', strict_validation=True, validate_responses=True)

    settings.init_app(app, **config)
    settings.load_extensions(app)

    return app
