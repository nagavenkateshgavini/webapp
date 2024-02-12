import pytest
from app import create_app

from config import Config


@pytest.fixture
def client():
    app = create_app(config_class=Config)
    app.config['TESTING'] = True
    return app.test_client()


def test_healthcheck(client):
    response = client.get('/healthz')
    assert response.status_code == 200

