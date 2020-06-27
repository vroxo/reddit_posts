from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_app(app: Flask):
    """
    Init database
    :param app: Flask
    """
    db.init_app(app)
