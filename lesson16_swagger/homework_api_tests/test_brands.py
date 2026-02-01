import requests

BRANDS = "/api/brands/"


def test_get_brands_public(base_url):
    r = requests.get(f"{base_url}{BRANDS}")
    assert r.status_code == 200


def test_create_brand_unauthorized(base_url):
    payload = {"name": "TestBrand"}
    r = requests.post(f"{base_url}{BRANDS}", json=payload)
    assert r.status_code in (401, 403)
