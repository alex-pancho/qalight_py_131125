import pytest
from conn_to_db import flatten, check_age
from lesson10_filetypes.ls10_json import read_json
from pathlib import Path

def add(a, b):
    return a + b

def test_add_a():
    actual_result = add(1, 1)
    expected_result = 2
    assert actual_result == expected_result, f"sum 1+1 != {expected_result}"

def test_flatten_simple():
    incoming_data = [1, 2, 3]
    actual_result = flatten(incoming_data)
    expected_result = [1, 2, 3]
    assert actual_result == expected_result

def test_check_age():
    actual_result = check_age(17)
    expectd_result = 17
    assert actual_result == expectd_result
    actual_result = check_age(0)
    expectd_result = 0
    assert actual_result == expectd_result
    actual_result = check_age(149)
    expectd_result = 149
    assert actual_result == expectd_result

def test_check_age_negative():
    with pytest.raises(ValueError):
        check_age(-1)
    with pytest.raises(ValueError):
        check_age(150)

def test_json_read():
    my_dir = Path(__file__).parent
    load_file = my_dir / "login.json"
    out_json = read_json(load_file)
    expected_json = {"login":
        {"description":"This is a sample login to Petstore server",
        "name":"harry_potter", "password":"DieTomRedlle!D1e",
        "termsOfService":"http://hogwards.io/terms/",
        "contact":{"email":"info@hogwards.io"},
        "license":{"name":"Apache 2.0","url":"http://www.apache.org/licenses/LICENSE-2.0.html"}
        }
    }
    assert out_json == expected_json