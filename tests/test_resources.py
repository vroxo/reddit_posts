import pytest


class TestResources:
    @pytest.fixture
    def json_valid(self):
        return {
            'init_date': '01/06/2020',
            'end_date': '05/06/2020',
            'order': 'ups'
        }

    def test_post_hot_posts_status_200(self, client, json_valid):
        response = client.post('api/v1/hot-posts', json=json_valid)
        assert response.status_code == 200

    def test_post_hot_posts_order_ups(self, client, json_valid):
        response = client.post('api/v1/hot-posts', json=json_valid)
        data = response.json['data']
        assert data[0]['title'] == 'Post 2'
        assert data[0]['ups'] == 5
        assert data[-1]['title'] == 'Post 6'
        assert data[-1]['ups'] == 0

    def test_post_hot_posts_order_comments(self, client, json_valid):
        json_valid['order'] = 'comments'
        response = client.post('api/v1/hot-posts', json=json_valid)
        data = response.json['data']
        assert data[0]['title'] == 'Post 3'
        assert data[0]['comments'] == 20
        assert data[-1]['title'] == 'Post 6'
        assert data[-1]['comments'] == 0

    def test_post_hot_posts_json_invalid(self, client, json_valid):
        del json_valid['init_date']
        response = client.post('api/v1/hot-posts', json=json_valid)
        assert response.status_code == 400

    def test_post_hot_posts_property_order_not_valid(self, client, json_valid):
        json_valid['order'] = 'xpto'
        response = client.post('api/v1/hot-posts', json=json_valid)
        assert response.status_code == 400
        assert response.json['error']

    def test_get_users_ups_status_200(self, client):
        response = client.get('api/v1/users/ups')
        assert response.status_code == 200

    def test_get_users_comments_status_200(self, client):
        response = client.get('api/v1/users/comments')
        assert response.status_code == 200

    def test_json_generic_response(self, client, json_valid):
        response_get = client.get('api/v1/users/ups')
        response_post = client.post('api/v1/hot-posts', json=json_valid)

        assert 'data' in response_get.json
        assert 'error' in response_get.json
        assert 'message' in response_get.json

        assert 'data' in response_post.json
        assert 'error' in response_post.json
        assert 'message' in response_post.json


