from flask import Flask
from . import connexion
from .ext import commands


def create_app() -> Flask:
    """
    Create a Flask object app by connexion
    :return: Flask
    """
    connexion.add_api('swagger.yaml', strict_validation=True, validate_responses=True)
    commands.init_app(connexion.app)
    return connexion.app
