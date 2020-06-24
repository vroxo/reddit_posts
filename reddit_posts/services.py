import requests
from .helpers import GenericHelper


class RedditService:
    def __init__(self):
        self.__uri = 'https://api.reddit.com/r/artificial/hot'

    def get_hot_posts(self):
        response = requests.get(self.__uri)

        if response.status_code != 200:
            raise RuntimeError(f'Error when get "hot posts" on reddit API - {response.json()}')

        response_data = response.json()['data']
        response_id = response_data.get('after')  # TODO Persist response id

        reddit_posts = response_data.get('children')

        dtos = list(
            map(lambda d: GenericHelper.create_object_by_dict('reddit_posts.dto.RedditServiceDto', d.get('data')),
                reddit_posts))

        return dtos
