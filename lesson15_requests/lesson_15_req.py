import requests

def get_method(url:str = "https://www.example.com", params:dict={}):
    """ Getting data... """
    response = requests.get(url, params=params)
    return response


def post_method(url:str = "https://www.example.com", data_to_send:dict = {}):
    """ Getting data... """
    response = requests.post(url, json=data_to_send)
    return response


def put_method(url:str = "https://www.example.com", data_to_send:dict = {}):
    """ Getting data... """
    response = requests.put(url, json=data_to_send)
    return response



def get_olx():
    url = "https://www.olx.ua/uk/vishnevoe/q-%D0%BE%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F-android/"
    data = {
        "search[filter_float_price:from]": 365,
        "search[filter_float_price:to]": 700
    }
    return get_method(url, data)

def print_response(response):
    print("status code:", response.status_code)
    print("url:", response.url)
    print("headers:", response.headers)
    print("text:", response.text)


def get_jsonplaceholder():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {'postId': 1, 'email': 'Nikita@garfield.biz'}
    response = get_method(url, params)
    return response
    # try:
    #     return response.json()
    # except requests.exceptions.JSONDecodeError as e:
    #     print(e)
    #     return response.text


def post_jsonplaceholder():
    url = 'http://jsonplaceholder.typicode.com/posts'
    data_to_send = {
        'userId': 1,
        'title': 'Some title',
        'email': "Sincere@april.biz"
    }
    return post_method(url, data_to_send)


def post_pastebin():
    url = "https://pastebin.com/api/api_post.php"
    post_data = dict(
        api_dev_key = "ulMHuv-FlPEloav7EYTG3u4jRLqizgxJ",
        api_paste_code = "Ми вивчаємо запити у пітон",
        api_option = "paste",
    )
    return post_method(url, post_data)

# Створення сесії
session = requests.Session()
def use_session():
    # Встановлення cookies для сесії
    cookies = {'user_id': '12345', 'session_id': 'abcdef'}
    session.cookies.update(cookies)
    headers= {"Authorization": "Bearer: kldjusdih-jbJDGSJKGSJAG-sdr3cd-ss"}
    # Виконання запитів за допомогою сесії
    response = session.get('https://example.com/page1', headers=headers)
    return response


if __name__ == "__main__":
    # response = get_olx()
    # print_response(response)
    # url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
    # response = get_method(url)
    # response = post_jsonplaceholder()
    response = post_pastebin()
    print_response(response)
    #print(response.json())
    