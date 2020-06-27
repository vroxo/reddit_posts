from importlib import import_module
from dynaconf import FlaskDynaconf
from flask import Flask


def load_extensions(app):
    """
    Load all extensions defined in settings.toml for the application
    :param app: Flask
    """
    for extension in app.config.EXTENSIONS:
        mod = import_module(extension)
        mod.init_app(app)


def init_app(app: Flask, **config):
    """
    Apply settings on App
    :param app: Flask
    """
    FlaskDynaconf(app, **config)
