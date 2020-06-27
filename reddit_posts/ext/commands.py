import datetime
from flask import Flask
from ..services import RedditService
from reddit_posts.documents import *
from ..helpers import GenericHelper


def job_reddit_posts():
    service = RedditService()

    response_id, posts = service.get_hot_posts()
    response = Response.objects(code=response_id).first()

    if posts and not response:
        bulk_posts = list(
            map(lambda p: GenericHelper.create_object_by_dict('reddit_posts.documents.Post', p.to_json()), posts)
        )
        Post.objects.insert(bulk_posts)
        Response(code=response_id).save()


def populate_db():
    Post.objects.insert([
        Post(title='Post 1', author='Author', author_name='Author Name', created=datetime.datetime(2020, 2, 27), ups=10,
             comments=1),
        Post(title='Post 2', author='Author2', author_name='Author Name 2', created=datetime.datetime(2020, 6, 1),
             ups=5,
             comments=10),
        Post(title='Post 3', author='Author3', author_name='Author Name 3', created=datetime.datetime(2020, 6, 2),
             ups=3,
             comments=20),
        Post(title='Post 4', author='Author4', author_name='Author Name 4', created=datetime.datetime(2020, 2, 3),
             ups=70,
             comments=0),
        Post(title='Post 5', author='Author5', author_name='Author Name 5', created=datetime.datetime(2020, 6, 4),
             ups=0,
             comments=11),
        Post(title='Post 6', author='Author6', author_name='Author Name 6', created=datetime.datetime(2020, 6, 5),
             ups=0,
             comments=0)

    ])

    Response(code='code_response').save()


def truncate_db():
    Post.drop_collection()
    Response.drop_collection()


def init_app(app: Flask):
    """
    Add commands on app
    :param app: Flask
    """
    for command in [job_reddit_posts, populate_db, truncate_db]:
        app.cli.add_command(app.cli.command()(command))
