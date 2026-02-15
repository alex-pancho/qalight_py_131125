import requests
import pytest

'''Test 1. Get My user Info. 
Should be executed for a new user only, before any changes with put and patch.'''
def test_get_me(api_base_url, auth_headers, get_method):
    url = f"{api_base_url}/api/users/me/"
    resp = get_method(url, headers=auth_headers)
    extected_data = {
        'id': 3, 
        'username': 'Nata', 
        'email': 'natali20151520@ukr.net', 
        'name': '', 
        'lastName': '', 
        'photoFilename': 'default-user.png', 
        'dateBirth': None, 
        'country': '', 
        'currency': 'usd', 
        'distance_units': 'km'}
    assert resp.status_code == 200
    assert resp.json() == extected_data


'''Test 2. Get brands'''
def test_get_brands(api_base_url, auth_headers, get_method):
    url = f"{api_base_url}/api/brands/"
    resp = get_method(url, headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    actual_titles = [brand["title"] for brand in data["results"]]
    expected_brands = {"AUDI", "BMW", "Ford"}
    assert expected_brands.issubset(set(actual_titles)), f"Expected brands {expected_brands} not found in {actual_titles}"
    

'''Test 3. Add a new brand'''
def test_add_brand(api_base_url, auth_headers, post_method):
    url = f"{api_base_url}/api/brands/"
    brand_name = "TESLA"
    data = {
        'title': brand_name
    }
    resp = post_method(url, data_to_send=data, headers=auth_headers)
    assert resp.status_code == 201
    resp_data = resp.json()
    assert resp_data["title"] == brand_name, f"Expected title {brand_name}, but got {resp_data.get('title')}"
    assert "id" in resp_data, "Server did not return ID for the new brand"
    print(f"\nBrand {brand_name} added with ID: {resp_data['id']}")

    
'''Test 4. Get cars
Pre-Conditions: 6 cars should be created.
This test should be written in cycle "add cars - get cars - delete cars" '''
def test_get_cars(api_base_url, auth_headers, get_method):
    url = f"{api_base_url}/api/cars/"
    resp = get_method(url, headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    actual_brands = [car["brand"] for car in data["results"]]
    expected_brands = {"AUDI", "BMW", "Ford"}
    assert expected_brands.issubset(set(actual_brands)), f"Expected brands {expected_brands} not found in {actual_brands}"
    assert data["count"] >= 6
    print(f"\nFound {len(actual_brands)} cars in the list.")


'''Test 5. Get models'''
def test_get_models(api_base_url, auth_headers, get_method):
    url = f"{api_base_url}/api/models/"
    resp = get_method(url, headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    actual_model_titles = [model["title"] for model in data["results"]]
    expected_models = {"Corvette", "Passadena", "Kuga"}
    assert expected_models.issubset(set(actual_model_titles)), f"Expected models {expected_models} not found in {actual_model_titles}"
    assert data["count"] >= 3
    print(f"\nSuccessfully verified {len(actual_model_titles)} models.")
    

'''Test 6. Post a new model'''
def test_add_car_model(api_base_url, auth_headers, post_method):
    url = f"{api_base_url}/api/models/"
    brand_id = 4
    model_name = "Focus"
    data = {
        'car_brand': brand_id,
        'title': model_name
    }
    resp = post_method(url, data_to_send=data, headers=auth_headers)
    assert resp.status_code == 201
    resp_data = resp.json()
    assert resp_data["title"] == model_name, f"Expected title {model_name}, but got {resp_data.get('title')}"
    assert "id" in resp_data, "Server did not return ID for the new model"
    assert resp_data["car_brand"] == brand_id, f"Expected brand ID {brand_id}, but got {resp_data.get('car_brand')}"
    print(f"\nModel '{model_name}' added successfully with ID: {resp_data['id']}")


'''Test 7. Post Ford car'''
def test_add_car(api_base_url, auth_headers, post_method):
    url = f"{api_base_url}/api/cars/"
    brand_id = 4
    model_id = 4    # id for Focus from Test 6
    initial_mileage = 10
    mileage = 100
    data = {
            "car_brand": brand_id,
            "car_model": model_id,
            "initial_mileage": initial_mileage,
            "mileage": mileage
            }
    resp = post_method(url, data_to_send=data, headers=auth_headers)
    assert resp.status_code == 201, f"Failed to create car: {resp.text}"
    resp_data = resp.json()
    assert resp_data["car_brand"] == brand_id, f"Expected brand ID {brand_id}, got {resp_data.get('car_brand')}"
    assert resp_data["car_model"] == model_id, f"Expected model ID {model_id}, got {resp_data.get('car_model')}"
    assert resp_data["initial_mileage"] == initial_mileage
    assert resp_data["mileage"] == mileage
    assert "id" in resp_data
    print(f"\nCar created successfully with ID: {resp_data['id']}")    
    

'''Test 8. Get model by id'''
def test_get_model_by_id(api_base_url, auth_headers, get_method):    
    model_id = 3
    url = f"{api_base_url}/api/models/{model_id}/"
    resp = get_method(url, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Kuga"
    assert resp.json()["id"] == 3