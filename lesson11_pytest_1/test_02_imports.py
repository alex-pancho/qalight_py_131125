from app.calc import add, is_even, divide


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


def test_divide_posivive():
    num_1 = 11
    num_2 = 2
    expected_result = 5.5
    actual_result = round(divide(num_1, num_2), 2)
    assert actual_result == expected_result


def test_is_even_positive():
    assert is_even(2)
    assert is_even(8) is True
    assert not is_even(3)
    assert is_even(9) is False
