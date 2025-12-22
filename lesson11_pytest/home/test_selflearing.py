import pytest
from selflearning02 import (greeting, calculate_area, is_even, create_profile, calculate_price, sum_all,
create_student, flexible_function, check_type_vs_isinstance, sort_vs_sorted_demo, filter_and_process,
create_multiplier, advanced_calculator)

"""
📝 Завдання 1. greeting(name)
Створи тести для функції, яка повертає "Привіт, {name}!"
Ідеї тестів:
- передати звичайне ім'я ("Оля")
- передати пустий рядок
- передати ім'я з пробілами ("Іван Петренко")
"""
def test_greeting():
    assert greeting("Оля") == "Привіт, Оля!"
    assert greeting("") == "Привіт, !"
    assert greeting("Іван Петренко") == "Привіт, Іван Петренко!"

"""
📝 Завдання 2. calculate_area(length, width)
Ідеї тестів:
- звичайні позитивні числа (5, 3)
- одне з чисел = 0
- дробові числа (2.5, 4.2)
"""
def test_calculate_area():
    assert calculate_area(5, 3) == 15
    assert calculate_area(0, 10) == 0
    assert calculate_area(2.5, 4.2) == pytest.approx(10.5)

"""
📝 Завдання 3. is_even(number)
Ідеї тестів:
- парне число (4)
- непарне число (7)
- від’ємне парне (-2)
- від’ємне непарне (-3)
"""
def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(-2) is True
    assert is_even(-3) is False

"""
📝 Завдання 4. create_profile(name, age, city, profession)
Ідеї тестів:
- передати тільки name і age
- передати всі аргументи
- не передати city/profession → має бути "Не вказано"
"""
def test_create_profile():
    profile1 = create_profile("Anna", 25)
    assert profile1["city"] == "Не вказано"
    assert profile1["profession"] == "Не вказано"

    profile2 = create_profile("Ted", 30, "Kyiv", "Coach")
    assert profile2 == {"name": "Ted", "age": 30, "city": "Kyiv", "profession": "Coach",}

"""
📝 Завдання 5. calculate_price(base_price, discount, tax)
Ідеї тестів:
- без знижки, стандартний податок
- зі знижкою 10%
- з нульовим податком
- з великою знижкою (наприклад 100%)
"""
def test_calculate_price():
    assert calculate_price(100) == 120.0
    assert calculate_price(100, discount=0.1) == 108.0
    assert calculate_price(100, tax=0) == 100.0
    assert calculate_price(100, discount=1) == 0.0

"""
📝 Завдання 6. sum_all(*args)
Ідеї тестів:
- кілька чисел (1, 2, 3, 4)
- без аргументів → 0
- суміш цілих і дробових
"""
def test_sum_all():
    assert sum_all(1, 2, 3, 4) == 10
    assert sum_all() == 0
    assert sum_all(1.5, 2, 3.5) == 7.0

"""
📝 Завдання 7. create_student(**kwargs)
Ідеї тестів:
- передати тільки name і age
- передати додаткові параметри (group="A1")
- не передати name → має бути значення за замовчуванням
"""
def test_create_student():
    s1 = create_student(name="Bob", age=20)
    assert s1["name"] == "Bob"
    assert s1["age"] == 20

    s2 = create_student(name="Bob", age=20, group="A1")
    assert s2["group"] == "A1"

    s3 = create_student(age=18)
    assert s3["name"] == "Unknown"

"""
📝 Завдання 8. flexible_function(*args, **kwargs)
Ідеї тестів:
- кілька позиційних аргументів
- тільки ключові аргументи
- суміш args і kwargs
"""
def test_flexible_function():
    args, kwargs = flexible_function(1, 2, 3)
    assert args == [1, 2, 3]
    assert kwargs == {}

    args, kwargs = flexible_function(name="John")
    assert args == []
    assert kwargs == {"name": "John"}

    args, kwargs = flexible_function(1, "hi", age=25)
    assert args == [1, "hi"]
    assert kwargs["age"] == 25

"""
📝 Завдання 9. Лямбда-функції
Ідеї тестів:
- square(4) == 16
- is_greater_than_10(5) == False
- concatenate("Hello", "World") == "HelloWorld"
"""
def test_lambdas():
    square = lambda x: x ** 2
    is_greater_than_10 = lambda x: x > 10
    concatenate = lambda x, y: x + y

    assert square(4) == 16
    assert is_greater_than_10(5) is False
    assert concatenate("Hello", "World") == "HelloWorld"

"""
📝 Завдання 10. check_type_vs_isinstance(value, check_type)
Ідеї тестів:
- int і перевірка на int
- bool і перевірка на int (type() ≠, але isinstance() =)
- str і перевірка на str
"""
def test_check_type_vs_isinstance():
    assert check_type_vs_isinstance(5, int) == (True, True)
    assert check_type_vs_isinstance(True, int) == (False, True)
    assert check_type_vs_isinstance("hi", str) == (True, True)

"""
📝 Завдання 11. sort_vs_sorted_demo(numbers)
Ідеї тестів:
- невідсортований список
- список уже відсортований
- список з від’ємними числами
"""
def test_sort_vs_sorted_demo():
    original = [3, 1, 2]
    sorted_list, sorted_copy = sort_vs_sorted_demo(original)

    assert sorted_list == [1, 2, 3]
    assert sorted_copy == [1, 2, 3]

"""
📝 Завдання 12. filter_and_process(data, filter_func, process_func)
Ідеї тестів:
- filter_func = lambda x: x > 0, process_func = lambda x: x*2
- фільтрація всіх елементів
- фільтрація, що нічого не залишає
"""
def test_filter_and_process():
    data = [1, 2, 3]
    result = filter_and_process(data, lambda x: x > 0, lambda x: x * 2)
    assert result == [2, 4, 6]

    result = filter_and_process(data, lambda x: False, lambda x: x * 2)
    assert result == []

"""
📝 Завдання 13. create_multiplier(factor)
Ідеї тестів:
- multiplier_2 = create_multiplier(2), multiplier_2(5) == 10
- multiplier_0 = create_multiplier(0), будь-яке число → 0
- multiplier_neg = create_multiplier(-1), має змінювати знак
"""
def test_create_multiplier():
    m2 = create_multiplier(2)
    assert m2(5) == 10

    m0 = create_multiplier(0)
    assert m0(100) == 0

    m_neg = create_multiplier(-1)
    assert m_neg(7) == -7

"""
📝 Завдання 14. advanced_calculator(*args, operation="...")
Ідеї тестів:
- сума чисел
- множення чисел
- максимум
- мінімум
- виклик без аргументів
"""
def test_advanced_calculator():
    assert advanced_calculator(1, 2, 3) == 6
    assert advanced_calculator(2, 3, operation="multiply") == 6
    assert advanced_calculator(5, 1, 9, operation="max") == 9
    assert advanced_calculator(5, 1, 9, operation="min") == 1
