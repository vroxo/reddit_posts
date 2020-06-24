from flask import Flask
from ..services import RedditService


def job_reddit_posts():
    service = RedditService()
    service.get_hot_posts()


def init_app(app: Flask):
    """
    Add commands on app
    :param app: Flask
    """
    for command in [job_reddit_posts]:
        app.cli.add_command(app.cli.command()(command))
