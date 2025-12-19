import pytest
from app.bank import calculate_discount
from app.calc import divide, is_even

# Тестуємо класи еквівалентності
def test_vip_discount():
    assert calculate_discount(100, "VIP") == 80

def test_student_discount():
    assert calculate_discount(100, "Student") == 90

def test_no_discount():
    assert calculate_discount(100, "Regular") == 100

# Тестуємо граничні значення
def test_zero_price():
    assert calculate_discount(0, "VIP") == 0

def test_small_price():
    actual_result = calculate_discount(0.01, "Student")
    assert round(actual_result, 3) == 0.009 # НЕ ПОРІВНЮВАТИ НАПРЯМУ! ТІЛЬКИ З round()


def test_negative_price_error():
    # Перевіряємо, що при ціні -100 виникне помилка ValueError
    with pytest.raises(ValueError) as excinfo:
        calculate_discount(-100, "VIP")
    
    # Можна також перевірити текст повідомлення в помилці
    assert str(excinfo.value) == "Ціна не може бути від'ємною"


def test_negative_divide():
    a = 2
    b = 0
    with pytest.raises(ValueError) as excinfo:
        divide(a, b)
    
    assert str(excinfo.value) == "Cannot divide by zero"

# 0, 2, 3, 5
@pytest.mark.parametrize(
        "number, expected",
        [
            (0, True),
            (2, True),
            (3, False),
            (5, False),
        ]
)
def test_is_even(number, expected):
    # number = 0
    # expected = True
    actual_result = is_even(number)
    assert actual_result == expected


@pytest.fixture
def default_user():
    # Підготовка даних
    user = {"name": "Ivan", "role": "admin", "balance": 100}
    return user

# Передаємо назву фікстури як аргумент у тест
def test_user_name(default_user):
    assert default_user["name"] == "Ivan"

def test_user_balance(default_user):
    assert default_user["balance"] > 0

def test_user_role(default_user):
    assert default_user["role"] in ["admin", "user"]