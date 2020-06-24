from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_app(app: Flask):
    """
    Init database and migrates
    :param app: Flask
    """
    db.init_app(app)
    Migrate(app, db)
