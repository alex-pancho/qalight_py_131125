import pytest
from app.calc import is_even
from app.bank import (
    calculate_discount,
)
from conftest import get_data
#from app import bank

# Тестуємо класи еквівалентності
def test_vip_discount():
    assert calculate_discount(100, "VIP") == 80


def test_student_discount():
    assert calculate_discount(100, "Student") == 90


def test_no_discount():
    assert calculate_discount(100, "Regular") == 100

# Граничні значення
def test_zero_price():
    assert calculate_discount(0, "VIP") == 0


def test_small_price():
    actual_result = calculate_discount(0.01, "Student")
    assert round(actual_result, 3) == 0.009 # НЕ ПОРІВНЮВАТИ НАПРЯМУ! ТІЛЬКИ З round()


# Тест на помилку
def test_negative_price_error():
    # Перевіряємо, що при ціні -100 виникне помилка ValueError
    with pytest.raises(ValueError) as excinfo:
        calculate_discount(-100, "VIP")
    
    # Можна також перевірити текст повідомлення в помилці
    assert str(excinfo.value) == "Ціна не може бути від'ємною"

@pytest.mark.parametrize(
        "number, expected",
        get_data()
)
def test_is_even_positive(number, expected):
    # number = 2
    # expected = True
    actual_result = is_even(number)
    assert actual_result == expected


# @pytest.fixture
# def default_user():
#     # Підготовка даних
#     user = {"name": "Ivan", "role": "admin", "balance": 100}
#     return user
@pytest.mark.smoke
# Передаємо назву фікстури як аргумент у тест
def test_user_name(default_user):
    assert default_user["name"] == "Ivan"

def test_user_balance(default_user):
    assert default_user["balance"] > 0

def test_user_role(default_user):
    assert default_user["role"] in ["admin", "user"]
