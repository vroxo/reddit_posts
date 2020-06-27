import datetime
from reddit_posts.documents import *


class TestPost:
    def test_post_to_json(self):
        p = Post(title='Title', author='author_fullname', author_name='author',
                 created=datetime.datetime(2020, 6, 26), ups=10, comments=10)
        assert p.to_json() == dict(title='Title', author='author_fullname', author_name='author',
                                   created=datetime.datetime(2020, 6, 26), ups=10, comments=10)
