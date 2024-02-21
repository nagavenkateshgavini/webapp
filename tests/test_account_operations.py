import base64
import time
from flask_testing import TestCase
from faker import Faker

from app import create_app
from config import Config

fake = Faker()


class TestAccountOperations(TestCase):

    def create_app(self):
        app = create_app(config_class=Config)
        return app

    @staticmethod
    def generate_random_username():
        return fake.email()

    def get_user_data(self, username=None):
        if username is None:
            username = self.generate_random_username()

        data = {
            "username": username,
            "password": "R@123d45jn",
            "first_name": "sai kumar",
            "last_name": "wow"
        }

        return data

    def create_account(self, data):
        response = self.client.post('/v1/user', json=data)
        assert response.status_code == 201

    @staticmethod
    def get_basic_auth_headers(username, password):
        auth_str = f"{username}:{password}"
        encoded_auth_str = base64.b64encode(auth_str.encode()).decode('utf-8')
        return {'Authorization': f'Basic {encoded_auth_str}'}

    def test_user_apis(self):
        # create account
        data = self.get_user_data()
        self.create_account(data)

        # get api
        response = self.client.get(
            '/v1/user/self',
            headers=self.get_basic_auth_headers(
                data["username"], data["password"])
        )

        assert response.status_code == 200
        assert response.json["username"] == data["username"]
        assert response.json["first_name"] == data["first_name"]
        assert response.json["last_name"] == data["last_name"]
        assert 'account_updated' in response.json
        assert 'account_created' in response.json

        # update api
        res_user_name = response.json["username"]
        password = data['password']

        updated_data = {
            "first_name": "python",
            "last_name": "pip"
        }

        # add sleep to check the account_updated value
        time.sleep(3)
        update_response = self.client.put('/v1/user/self', json=updated_data,
                                          headers=self.get_basic_auth_headers(res_user_name, password))
        assert update_response.status_code == 204

        update_response = self.client.get(
            '/v1/user/self',
            headers=self.get_basic_auth_headers(res_user_name, password)
        )

        assert update_response.status_code == 200
        assert update_response.json["username"] == res_user_name
        assert update_response.json["first_name"] == updated_data["first_name"]
        assert update_response.json["last_name"] == updated_data["last_name"]
        assert 'account_updated' in update_response.json
        assert 'account_created' in update_response.json
        assert update_response.json["account_created"] != update_response.json["account_updated"]

    def test_health_check(self):
        response = self.client.get('/healthz')
        assert response.status_code == 200
        assert response.data == b''

        response = self.client.post('/healthz')
        assert response.status_code == 405


# Run the tests
# pytest -v test_account_operations.py
