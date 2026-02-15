import requests
import pytest

@pytest.fixture(scope="module")
def get_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.get(url, params=data_to_send, headers=headers)
    return response

def post_method(url:str = "https://www.example.com", data_to_send:dict = {}, headers={}):
    """ Getting data... """
    response = requests.post(url, json=data_to_send, headers=headers)
    return response

def auth_signin(username:str, password:str, headers={}):
    endpoint = "/api/auth/signin/"
    #base_url = "http://127.0.0.1:8000"
    base_url = "https://car-service-api-and-ui.onrender.com/"
    test_url = base_url + endpoint
    data = {
        "username": username,
        "password": password 
    }
    resp = post_method(test_url, data, headers=headers)
    # print(f'Status code: {resp.status_code}')
    # print(resp.json())
    return resp
if __name__ == "__main__":
    print("Test 1: My user Singin")
    auth_signin("Nata", "test123password")