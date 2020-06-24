from dynaconf import FlaskDynaconf
from flask import Flask


def init_app(app: Flask):
    """
    Apply settings on App
    :param app: Flask
    """
    FlaskDynaconf(app)
