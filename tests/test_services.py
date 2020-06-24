import pytest

from reddit_posts.dto import RedditServiceDto
from reddit_posts.services import RedditService


class TestServices:
    @pytest.fixture()
    def response(self, mocker):
        response = mocker.patch('reddit_posts.services.requests.Response')
        response.status_code = 200
        response.json.return_value = {'data': {'after': 't3_hdyiaf',
                                               'children': [{'data': {
                                                   'title': "Welcome to /r/artificial!",
                                                   'author_fullname': "t2_3dncp",
                                                   'author': "CyberByte",
                                                   'created': 1497932195,
                                                   'ups': 100,
                                                   'num_comments': 3
                                               }}]}
                                      }
        return response

    def test_get_hot_posts(self, mocker, response):
        mocker.patch('reddit_posts.services.requests.get', return_value=response)
        posts = RedditService().get_hot_posts()
        for post in posts:
            assert isinstance(post, RedditServiceDto)

    def test_get_hot_posts_error(self, mocker, response):
        response.status_code = 404
        response.json.return_value = {'error': True, 'message': 'Not found!'}
        with pytest.raises(RuntimeError):
            RedditService().get_hot_posts()
