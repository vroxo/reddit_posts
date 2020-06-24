import pytest
from reddit_posts.dto import RedditServiceDto
from reddit_posts.helpers import GenericHelper


class TestGenericHelper:
    def test_create_object_by_dict(self):
        o = GenericHelper.create_object_by_dict('reddit_posts.dto.RedditServiceDto',
                                                dict(title='Teste', author_fullname='user_id', author='Vitor',
                                                     created=1497932195, ups=0,
                                                     num_comments=0))

        assert isinstance(o, RedditServiceDto)

    def test_module_error_create_object_by_not_dict(self):
        with pytest.raises(RuntimeError):
            GenericHelper.create_object_by_dict('xpto', dict(teste='Teste'))
