import requests
import uuid

SIGNUP = "/api/auth/signup/"
SIGNIN = "/api/auth/signin/"
REFRESH = "/api/auth/refresh/"


def test_signup_success(base_url):
    """
    Positive signup test.
    Signup requires full schema: username, names, email, password, repeatPassword.
    """
    password = "TestPass123!"
    user = {
        "username": f"user_{uuid.uuid4().hex[:6]}",
        "first_name": "Test",
        "last_name": "User",
        "email": f"user_{uuid.uuid4().hex[:6]}@test.com",
        "password": password,
        "repeatPassword": password,
    }

    r = requests.post(f"{base_url}{SIGNUP}", json=user)
    assert r.status_code in (200, 201), r.text


def test_signin_success(base_url, valid_user):
    """
    Positive signin with existing user.
    """
    r = requests.post(f"{base_url}{SIGNIN}", json=valid_user)
    assert r.status_code == 200


def test_signin_wrong_password(base_url, valid_user):
    """
    Negative signin: wrong password.
    """
    bad_user = {
        "username": valid_user["username"],
        "password": "WrongPass123"
    }
    r = requests.post(f"{base_url}{SIGNIN}", json=bad_user)
    assert r.status_code in (400, 401)


def test_refresh_with_valid_token(base_url, valid_user):
    """
    Positive refresh flow:
    signin -> refresh -> new access token
    """
    # signin
    r_login = requests.post(f"{base_url}{SIGNIN}", json=valid_user)
    assert r_login.status_code == 200
    tokens = r_login.json()

    refresh_token = tokens.get("refresh")
    assert refresh_token, f"No refresh token in response: {tokens}"

    # refresh
    r_refresh = requests.post(
        f"{base_url}{REFRESH}",
        json={"refresh": refresh_token}
    )
    assert r_refresh.status_code == 200
    assert "access" in r_refresh.json()
