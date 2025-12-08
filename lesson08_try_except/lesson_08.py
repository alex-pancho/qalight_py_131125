
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("I can't divide by zero!")
        result = None
    return result

print(divide(10, 0.0))
print("hello")

def divide_from_list(a:int, b:list):
    try:
        result = a / b[0]
    except (ZeroDivisionError):
        print("I can't divide by zero!")
        result = None
    except (IndexError, TypeError):
        print("Give a non-empty list")
        result = None
    return result

print(divide_from_list(10, [1]))
print(divide_from_list(10, [0]))
print(divide_from_list(10, []))
print(divide_from_list(10, 0))


def sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Do not use None here")
        return None
    
print(sum(10, "a"))


def mid_processor(list_store:list):
    list_len = len(list_store)
    index_of_mid_element = list_len // 2
    try:
        return list_store[index_of_mid_element]
    except (IndexError, ValueError):  # multi-exeption
        print("Empty list. Dont do it again!!!")
        # return 0
    except:
        print("Do smth here")

## while True:
##     try:
##         print("asas")
##     except:
##         pass # KeyboardInterrupt

def divide_numbers(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль.")
        return result
    else:
        "Блок else виконується, якщо в блоку try не виникло жодного виключення"
        print(f"Результат ділення {a} на {b}: {result}")
        return result
    finally:
        # наприклад збереження в файл
        print("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")

print(divide_numbers(3,0))


def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age


def check_email(mail:str):
    if not isinstance(mail, str):
        raise TypeError("Only String type is expected")
    if mail.count("@") < 1:
        raise ValueError("@ expected in mailbox")
    return mail


print(check_email("some@gmail.com"))
print(check_email("s@g.c"))
print(check_email("@"))
# print(check_email(""))
# print(check_email(1))

def sum_2(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "int, float is expected"
    return a + b

print(sum_2(1, 1))
print(sum_2(1, 1.111))
# print(sum_2(1,[1]))

# IndexError
# TypeError
# ValueError
# AssertionError
# ZeroDivisionError
