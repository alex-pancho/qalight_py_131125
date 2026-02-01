import requests

MODELS = "/api/models/"


def test_get_models_public(base_url):
    r = requests.get(f"{base_url}{MODELS}")
    assert r.status_code == 200


def test_create_model_unauthorized(base_url):
    payload = {"name": "TestModel"}
    r = requests.post(f"{base_url}{MODELS}", json=payload)
    assert r.status_code in (401, 403)
