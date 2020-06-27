import datetime
from reddit_posts.dto import RedditServiceDto


class TestRedditServiceDto:
    def test_dto_repr_(self):
        dto = RedditServiceDto('Title', 'author_fullname', 'author', 1497932195, 10, 10)
        assert dto.to_json() == dict(
            title='Title',
            author='author_fullname',
            author_name='author',
            created=datetime.datetime.fromtimestamp(1497932195),
            ups=10,
            comments=10
        )
