from flask import make_response, Response
import datetime
from ..documents import Post
from mongoengine import Q


def get_hot_posts(body: dict) -> Response:
    init_date = datetime.datetime.strptime(body['init_date'], '%d/%m/%Y')
    end_date = datetime.datetime.strptime(body['end_date'], '%d/%m/%Y')
    order = body['order']

    if not __is_order_valid(order):
        msg = "Invalid 'order' property value, choose between 'ups' or 'comments' values."
        return __make_generic_response(error=True,
                                       message=msg,
                                       status_code=400)

    posts = Post.objects(
        Q(created__gte=init_date) &
        Q(created__lte=end_date)
    ).order_by(f'-{order}')

    data = list()
    for post in posts:
        data.append(
            post.to_json()
        )

    return __make_generic_response(data=data)


def get_users(order: str) -> Response:
    if not __is_order_valid(order):
        msg = "Invalid 'order' property value, choose between 'ups' or 'comments' values."
        return __make_generic_response(error=True,
                                       message=msg,
                                       status_code=400)

    pipeline = [
        {
            '$group': {
                '_id': '$author',
                'user': {'$first': '$author_name'},
                'ups': {'$sum': '$ups'},
                'comments': {'$sum': '$comments'}
            }
        },
        {'$sort': {f'{order}': -1}}
    ]

    users = Post.objects().aggregate(pipeline)
    data = list()
    for user in users:
        del user['_id']
        data.append(user)

    return __make_generic_response(data, False, 'Success!', 200)


def __make_generic_response(data=None, error: bool = False, message: str = 'Success!',
                            status_code: int = 200) -> Response:
    if data is None:
        data = list()

    response = {
        'error': error,
        'message': message,
        'data': data
    }

    return make_response(response, status_code)


def __is_order_valid(order: str) -> bool:
    return 'ups' == order or 'comments' == order
