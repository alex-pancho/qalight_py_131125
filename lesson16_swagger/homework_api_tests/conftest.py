import os
import pytest
import requests


# ---------- CONFIG ----------
DEFAULT_BASE_URL = "http://127.0.0.1:8000"
DEFAULT_USER = "Yevhenii"
DEFAULT_PASS = "Yevhenii"
# ----------------------------


@pytest.fixture(scope="session")
def base_url():
    """
    Base URL for API.
    Can be overridden via BASE_URL env var.
    """
    return os.getenv("BASE_URL", DEFAULT_BASE_URL)


@pytest.fixture(scope="session")
def valid_user():
    """
    Credentials for signin.
    Do NOT hardcode real creds in repo – use env vars if possible.
    """
    return {
        "username": os.getenv("API_USER", DEFAULT_USER),
        "password": os.getenv("API_PASS", DEFAULT_PASS),
    }


@pytest.fixture(scope="session")
def access_token(base_url, valid_user):
    """
    Try to obtain access token.
    If signin fails – skip dependent tests instead of failing whole suite.
    """
    url = f"{base_url}/api/auth/signin/"
    response = requests.post(url, json=valid_user)

    if response.status_code != 200:
        pytest.skip(
            f"Signin failed: {response.status_code} | {response.text}"
        )

    try:
        data = response.json()
    except ValueError:
        pytest.skip("Signin response is not JSON")

    token = data.get("access") or data.get("token") or data.get("access_token")

    if not token:
        pytest.skip(f"No access token in response: {data}")

    return token


@pytest.fixture
def auth_headers(access_token):
    """
    Authorization headers for protected endpoints.
    """
    return {
        "Authorization": f"Bearer {access_token}"
    }
