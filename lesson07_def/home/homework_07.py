# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1
#     # Complete the while loop condition.
#     while multiplier <= number:
#         result = number * multiplier
#         # десь тут помилка, а може не одна
#         if  result > "25":
#             # Enter the action to take if the result is greater than 25
#             pass
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#         # Increment the appropriate variable
#         multiplier += 1
# multiplication_table(3)
def multiplication_table(number):
    for multiplier in range(1, 26):  # максимальний добуток 25, тому множник не більше 25
        result = number * multiplier
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
#----------------------------------------------------------------
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("\nTask_2")
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(3, 5))
#----------------------------------------------------------------
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\nTask_3")
def average_list(numbers):
    return sum(numbers) / len(numbers)
print(average_list([1, 2, 3, 4, 5]))
#-----------------------------------------------------------------
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\nTask_4")
def reverse_string(string):
    return string[::-1]
print(reverse_string("Привіт!"))
#----------------------------------------------------------------------
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\nTask_5")
def longest_word(words):
      return max(words, key=len)
print(longest_word(["кішка", "собака", "миша"]))
#-----------------------------------------------------------------------------
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
#---------------------------------------------------------------------------------
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# ЗАВДАННЯ 6: Математичні обчислення (Оригінал)
# print("\nЗавдання 6: Обчисліть площу та периметр прямокутника")
# width = 12.5
# height = 8.3
# # Ваш код тут:
# rectangle_area = width * height  # width * height
# rectangle_perimeter = 2 * (width + height)
#
# print(rectangle_area)
# print(rectangle_perimeter)
print("\nTask_7")
def rectangle_properties(width, height):
    area = round(width * height, 2)
    perimeter = 2 * (width + height)
    return area, perimeter
width, height = 12.5, 8.3
area, perimeter = rectangle_properties(width, height)
print(f"Площа дорівнює: {area}, Периметр дорівнює: {perimeter}")
#-------------------------------------------------------------------
# task 8
# ЗАВДАННЯ 10: Складні обчислення (Оригінал)
# print("\nЗавдання 10: Обчисліть складний вираз")
# x = 10
# y = 3
# z = 2
# # Ваш код тут:
# result1 = (x + y) * z  # (10 + 3) * 2
# result2 = x ** y - z  # 10 ** 3 - 2
# result3 = (x / y) + (z * 2)  # (10 / 3) + (2 * 2)
# result4 = x % y + z ** 2  # 10 % 3 + 2 ** 2
#
# print(result1)
# print(result2)
# print(result3)
# print(result4)
print("\nTask_8")
def complex_result(x, y, z):
    result1 = (x + y) * z
    result2 = x ** y - z
    result3 = round((x / y) + (z * 2), 2)
    result4 = x % y + z ** 2
    return result1, result2, result3, result4

x, y, z = (10, 3, 2)
res1, res2, res3, res4 = complex_result(x, y, z)
print(res1)
print(res2)
print(res3)
print(res4)
#-------------------------------------------------------------
# task 9
# Task 16. Створіть дві множини та знайдіть їх об'єднання (Оригінал)
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# union_set = set_a.union(set_b)  # Ваш код тут
# # union_set = set_a | set_b
# print("\nunion_set :", union_set)
print("\nTask_9")
def union_of_sets(set_a, set_b):
    return set_a | set_b
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = union_of_sets(set_a, set_b)
print("union_set:", union_set)
#-------------------------------------------------------------------
# task 10
# print("\n=== ЗАВДАННЯ 9: Пропуск непарних чисел ===") (Оригінал)
# # Виведіть тільки парні числа від 1 до 20, використовуючи continue
# print("Парні числа від 1 до 20:")
# # Ваш код тут:
# for number in range(1, 21):
#     if number % 2 != 0:
#         continue
#     print(f"Парне число: {number}")
print("\nTask_10")
def print_even_numbers(n):
    print(f"Парні числа від 1 до {n}:")
    for number in range(1, n + 1):
        if number % 2 != 0:
            continue
        print(f"Парне число: {number}")
print_even_numbers(20)
