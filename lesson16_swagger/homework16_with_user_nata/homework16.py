import requests
import pytest

def get_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.get(url, params=data_to_send, headers=headers)
    return response

def post_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.post(url, json=data_to_send, headers=headers)
    return response

'''Test 1. My user signin'''
def auth_signin(username:str, password:str, headers={}):
    endpoint = "/api/auth/signin/"
    #base_url = "http://127.0.0.1:8000"    # we also can login on local server
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint
    data = {
        "username": username,
        "password": password 
    }
    resp = post_method(test_url, data, headers=headers)
    print(f'Status code: {resp.status_code}')
    print(resp.json())
    return resp
if __name__ == "__main__":
    print("Test 1: My user Singin")
    auth_signin("Nata", "test123password")

'''Test 2. Get My user Info'''
def get_me(headers):
    endpoint = "/api/users/me/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    resp = get_method(test_url, headers=headers)
    
    print(f'Status code: {resp.status_code}')
    try:
        print(resp.json())
    except:
        print(resp.text)
    return resp

if __name__ == "__main__":
    print("Test 2: My user Info")
    # варіант 1 - токен захардкордили 
    # my_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcwOTg3NDYxLCJpYXQiOjE3NzA5ODcxNjEsImp0aSI6IjM1ZTEzOWNmNGRlNDQ4MjliNjM0MWZmNTVmYTA2NjRhIiwidXNlcl9pZCI6IjMifQ.DWIkxiXellYoyNZEhUnBcxkwuhlZ1owstQ4djZrX5FU' 
    # headers_for_request = {
    #     "Authorization": f"Bearer {my_token}"
    # }
    # get_me(headers_for_request)

    # варіант 2 - токен беремо з responce авторизації
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        get_me(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 3. Get brands'''
def get_brands(headers):
    endpoint = "/api/brands/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    resp = get_method(test_url, headers=headers)
    
    print(f'Status code: {resp.status_code}')
    try:
        print('Brands list:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 3: Get brands")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        get_brands(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 4. Add a new brand'''
def add_brand(headers, brand_name):
    endpoint = "/api/brands/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    data = {
        'title': brand_name
    }

    resp = post_method(test_url, data_to_send=data, headers=headers)
    print(f'Status code: {resp.status_code}')
    try:
        print('Responce:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 4: Add a new brand")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        add_brand(headers_for_request, "Ford")
        print('Updated Brands list:')
        get_brands(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 5. Get cars'''
def get_cars(headers):
    endpoint = "/api/cars/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    resp = get_method(test_url, headers=headers)
    
    print(f'Status code: {resp.status_code}')
    try:
        print('Cars list:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 5: Get cars")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        get_cars(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 6. Get models'''
def get_models(headers):
    endpoint = "/api/models/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    resp = get_method(test_url, headers=headers)
    
    print(f'Status code: {resp.status_code}')
    try:
        print('Cars list:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 6: Get models")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        get_models(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 7. Post Ford models'''
def add_car_model(headers, brand_id, model_name):
    endpoint = "/api/models/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    data = {
        'car_brand': brand_id,
        'title': model_name
    }

    resp = post_method(test_url, data_to_send=data, headers=headers)
    print(f'Status code: {resp.status_code}')
    try:
        print('Responce:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 7: Post Ford models")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        add_car_model(headers_for_request, 4, "Kuga")
        print('Updated Models list:')
        get_models(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 8. Post Ford car'''
def add_car(headers, brand_id, model_id, initial_mileage, mileage):
    endpoint = "/api/cars/"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint

    data = {
            "car_brand": brand_id,
            "car_model": model_id,
            "initial_mileage": initial_mileage,
            "mileage": mileage
            }
    resp = post_method(test_url, data_to_send=data, headers=headers)
    print(f'Status code: {resp.status_code}')
    try:
        print('Responce:', resp.json())
    except:
        print('Raw responce:', resp.text)
    return resp

if __name__ == "__main__":
    print("Test 8: Post Ford car")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    if token:
        headers_for_request = {
            "Authorization": f"Bearer {token}"
        }
        add_car(headers_for_request, 4, 3, 5, 500)
        print('Updated Cars list:')
        get_cars(headers_for_request)
    else:
        print("Помилка: не вдалося отримати токен!")


'''Test 9. Get model by id'''
def get_model_by_id(headers, model_id):    
    endpoint = f"/api/models/{model_id}/"
    base_url = "https://car-service-api-and-ui.onrender.com"
    test_url = base_url + endpoint
    resp = get_method(test_url, headers=headers)
    print(f"Status code: {resp.status_code}")
    
    try:
        data = resp.json()
        print("Model Data:", data)
        return data
    except Exception:
        print("Raw response:", resp.text)
        return None
    
if __name__ == "__main__":
    print("Test 9: Get model by id")
    login_resp = auth_signin("Nata", "test123password")
    token = login_resp.json().get('access') 
    
    if token:
        headers_for_request = {"Authorization": f"Bearer {token}"}
        get_model_by_id(headers_for_request, 3)
    else:
        print("Помилка авторизації")