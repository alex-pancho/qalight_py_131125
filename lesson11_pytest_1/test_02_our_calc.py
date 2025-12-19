import math
# import requests # Сторонній модуль, який ми не встановили
from app.calc import add, divide
#from calc import add, divide #

def test_add_positive_numbers_details():
    """
    Тест з позитивними цілими (int) 
    """
    pos_num_1 = 2
    pos_num_2 = 3
    actual_result = add(pos_num_1, pos_num_2)
    expected_result = 5
    assert actual_result == expected_result


def test_add_negative_numbers():
    """
    Тест з позитивними цілими (int) 
    """
    neg_num_1 = -1
    neg_num_2 = -2
    actual_result = add(neg_num_1, neg_num_2)
    expected_result = -3
    assert actual_result == expected_result

def test_divide_posivive():
    num_1 = 10
    num_2 = 2
    expected_result = 5
    assert divide(num_1, num_2) == expected_result
