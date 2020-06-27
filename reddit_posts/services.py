import requests
from dynaconf import settings
from .helpers import GenericHelper


class RedditService:
    def __init__(self):
        self.__uri = settings.URI_REDDIT

    def get_hot_posts(self) -> tuple:
        response = requests.get(self.__uri, headers={'User-agent': __name__})

        if response.status_code != 200:
            raise RuntimeError(f'Error when get "hot posts" on reddit API - {response.json()}')

        response_data = response.json()['data']

        reddit_posts = response_data.get('children')

        dtos = list(
            map(lambda d: GenericHelper.create_object_by_dict('reddit_posts.dto.RedditServiceDto', d.get('data')),
                reddit_posts))

        response_id = response_data.get('after')
        return response_id, dtos
