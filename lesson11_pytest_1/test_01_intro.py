# 1. Функції, які ми хочемо протестувати (логіка)
def add(a, b):
    return a + b


def is_adult(age):
    return age >= 18


def test_add_positive_numbers():
    """
    Тест з позитивними цілими (int) 
    """
    assert add(2, 3) == 5


def test_add_positive_numbers_details():
    """
    Тест з позитивними цілими (int) 
    """
    pos_num_1 = 2
    pos_num_2 = 3
    expected_result = 5
    actual_result = add(pos_num_1, pos_num_2)
    assert actual_result == expected_result


def test_add_negative_numbers():
    """
    Тест з позитивними цілими (int) 
    """
    pos_num_1 = -2
    pos_num_2 = -3
    expected_result = -5
    actual_result = add(pos_num_1, pos_num_2)
    assert actual_result == expected_result


def test_add_positive_floats():
    """
    Тест з позитивними цілими (int) 
    """
    pos_num_1 = 1.1
    pos_num_2 = 2.2
    expected_result = 3.3
    actual_result = round(add(pos_num_1, pos_num_2), 2)
    assert actual_result == expected_result


def test_check_age_positive():
    correct_adult_age = 18
    assert is_adult(correct_adult_age) is True


def test_check_age_positive_second():
    correct_adult_age = 42
    actual_result = is_adult(correct_adult_age)
    assert actual_result is True, f"функція приймає значення {correct_adult_age} і повертає {actual_result} "


def test_check_age_positive_less():
    correct_adult_age = 17
    actual_result = is_adult(correct_adult_age)
    assert actual_result is False, f"функція приймає значення {correct_adult_age} і повертає {actual_result} "
