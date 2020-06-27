import datetime
import pytest
from reddit_posts.app import create_app
from reddit_posts.ext.commands import populate_db, truncate_db
from reddit_posts.documents import Post


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        populate_db()
        yield app
        truncate_db()


@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()

    yield client


@pytest.fixture(scope="session")
def posts(app):
    with app.app_context():
        return Post.objects()


@pytest.fixture(scope="session")
def planet(app):
    with app.app_context():
        post = Post(title='Post x', author='AuthorX', author_name='Author Name x',
                      created=datetime.datetime(2020, 2, 27), ups=30,
                      comments=200)
        post.save()
        return post
