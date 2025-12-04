
# a = 1
# b = 2
# # c = a + b
# # d = c + b
# # e = a + d

def print_song():
    """Друкує пісню"""
    print("Ой у лузі червона калина похилилася")
    print("Чогось наша славна Україна зажурилася")

print_song()

def hello(name):
    return f"{name} hello!"

output = hello("Ivan")
print(output)

def describe_pet(animal_type, pet_name) -> str:
    """Display information about a pet."""
    return f"My {animal_type}'s name is {pet_name.title()}."

print(describe_pet("dog", "rex"))

def greet(name: str, greeting: str = "Привіт"):
    """
    Функція виводить привітання для заданого імені.

    :param name: Ім'я для привітання
    :param greeting: Привітання (за замовчуванням "Привіт")
    """
    print(f"{greeting}, {name}!")

greet("Юрій")
greet("Оксана", "Доброго дня")
print(greet(""))

greet(greeting = "Hello", name = "Genna")
# позиційні - у порядку заданому у коді
# іменовані - ім'я = значення, 

def print_args(*args):
    for arg in args:
        print(arg)
print("=============")
print_args(1, "hello", None)
print("=============")
print_args(1, "hello", 3.14, [1, 2, 3])

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_kwargs(name="John", age=25, city="New York")
print("=============")
def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_args_and_kwargs(1, "hello", 3.14, name="John", age=25)

def minus(a, b):
    return a - b

print(minus(2, 5))
print(minus(5, 2))

print_args_and_kwargs(name="Inna", age=43)

def describe_person(name, age, country="Unknown"):
    print(f"{name} is {age} years old and is from {country}.")

describe_person("Alice", 30)  # Alice is 30 years old and is from Unknown.
describe_person("Bob", 25, country="USA")  # Bob is 25 years old and is from USA.

describe_person("Charlie", country="Canada", age=28)

# lambda arguments: expression

square = lambda x: x**2

print(square(5))

add = lambda x, y: x + y
print(add(3, 4))

print("============="*6)

print(all([1, 2, -4]))
print(all([1, 2, 0]))

print(any([1,2,3]))
print(any([0,2,0]))
print(any([0,0,0]))

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
# person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
#                ('David', 28), ('Emma', 22), ('Frank', 45)]
# out = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
# for name, age in person_list:
#     if 10 <= age <= 19:
#         out['10-19'].append(name)
# print(out)
byte_array = bytearray(b'Hello, World!')
byte_array[0] = 44  # bytearray змінний, тож 0 елемент
                    # змінюється на символ з кодом 37 == %
print(byte_array.decode('utf-8'))   # %ello, World!

print(chr(1111), chr(44))

my_dict = dict(a="a", b=[1,2])
print(my_dict)

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter(is_even, numbers)
even_numbers = list(filtered_numbers)
print(even_numbers)

value1 = "abc"
value2 = "DER"
formatted_string = "Some text {} and {}.".format(value1, value2)
print(formatted_string)

hello_my = "hello"  
print(id(hello_my))
hello_my = "ferer"
print(id(hello_my))
list_1 = []
print(id(list_1))
list_1.append(1)
print(id(list_1))

# value = input("Input value:")
# # str
print(int("73") == 73)

x = 5
print(isinstance(x, int))
print(isinstance(x, str))

print(len("len"))

print(max([3, 1, 4]))
print(min([3, 1, 4]))

print(pow(3, 3))

print(list(reversed([10, 2, 4])))

print(round(2.60))
print(round(2.40))

print(sorted((2, 4, 2, 3, 7)))
print(str(123))

print(sum([1, 2, 3]))

print(type("hello"))
