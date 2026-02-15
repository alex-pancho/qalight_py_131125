import pytest
import requests

BASE_URL = "https://car-service-api-and-ui.onrender.com"
LOGIN_DATA = {
    "username" : "Nata",
    "password" : "test123password" 
}

@pytest.fixture(scope="session")
def auth_token():
    url = f"{BASE_URL}/api/auth/signin/"
    response = requests.post(url, json=LOGIN_DATA)

    if response.status_code != 200:
        pytest.fail(f"No autorization: {response.status_code}, {response.text}")

    token = response.json().get('access')
    return token

@pytest.fixture(scope="function")
def auth_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def api_base_url():
    return BASE_URL

@pytest.fixture
def get_method():
    def _get(url, data_to_send=None, headers=None):
        return requests.get(url, params=data_to_send, headers=headers)
    return _get

@pytest.fixture
def post_method():
    def _post(url, data_to_send=None, headers=None):
        return requests.post(url, json=data_to_send, headers=headers)
    return _post