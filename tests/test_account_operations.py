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

    def create_account(self, username=None):
        if username is None:
            username = self.generate_random_username()

        data = {
            "username": username,
            "password": "R@123d45jn",
            "first_name": "sai kumar",
            "last_name": "wow"
        }
        response = self.client.post('/v1/user', json=data)
        assert response.status_code == 201
        return data

    @staticmethod
    def get_basic_auth_headers(username, password):
        auth_str = f"{username}:{password}"
        encoded_auth_str = base64.b64encode(auth_str.encode()).decode('utf-8')
        return {'Authorization': f'Basic {encoded_auth_str}'}

    def test_create_account(self):
        create_account_data = self.create_account()

        response = self.client.get(
            '/v1/user/self',
            headers=self.get_basic_auth_headers(
                create_account_data["username"], create_account_data["password"])
        )

        assert response.status_code == 200
        assert response.json["username"] == create_account_data["username"]
        assert response.json["first_name"] == create_account_data["first_name"]
        assert response.json["last_name"] == create_account_data["last_name"]
        assert 'account_updated' in response.json
        assert 'account_created' in response.json

    def test_update_account(self):
        create_account_data = self.create_account()
        updated_data = {
            "first_name": "python",
            "last_name": "pip"
        }

        # add sleep to check the account_updated value
        time.sleep(3)
        update_response = self.client.put('/v1/user/self', json=updated_data,
                                          headers=self.get_basic_auth_headers(create_account_data["username"],
                                                                              create_account_data["password"]))
        assert update_response.status_code == 204

        response = self.client.get(
            '/v1/user/self',
            headers=self.get_basic_auth_headers(
                create_account_data["username"], create_account_data["password"])
        )

        assert response.status_code == 200
        assert response.json["username"] == create_account_data["username"]
        assert response.json["first_name"] == updated_data["first_name"]
        assert response.json["last_name"] == updated_data["last_name"]
        assert 'account_updated' in response.json
        assert 'account_created' in response.json
        assert response.json["account_created"] != response.json["account_updated"]

    def test_get_user(self):
        create_account_data = self.create_account()

        response = self.client.get('/v1/user/self',
                                   headers=self.get_basic_auth_headers(create_account_data["username"],
                                                                       create_account_data["password"]))
        assert response.status_code == 200

# Run the tests
# pytest -v test_account_operations.py
