from flask import make_response


def index():
    return make_response({'error': False, 'message': 'index!'}, 200)
