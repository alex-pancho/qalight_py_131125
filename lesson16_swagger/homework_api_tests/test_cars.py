import requests

CARS = "/api/cars/"


def test_get_cars_unauthorized(base_url):
    r = requests.get(f"{base_url}{CARS}")
    assert r.status_code in (401, 403)


def test_get_cars_authorized(base_url, auth_headers):
    r = requests.get(f"{base_url}{CARS}", headers=auth_headers)
    assert r.status_code == 200
