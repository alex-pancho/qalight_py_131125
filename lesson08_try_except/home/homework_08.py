"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""
# def sum_numbers_in_list(string_list: list):
#     """Повертає список сум чисел зі списку строк,
#     які складаються з чисел, розділених комою."""
#     result = []
#     for item in string_list:
#         try:
#             pass
#         except ValueError as e:
#             result.append("Не можу це зробити!")
##     return result
print("\nTask_8\n")
def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку рядків,
    які складаються з чисел, розділених комою."""
    # Перевірка на правильний тип вхідних даних
    if not isinstance(string_list, list) or len(string_list) == 0:
        return "ValueError"
    result = []
    for item in string_list:
        try:
            if not isinstance(item, str):
                raise AttributeError("Елемент не є рядком")
            # Розділяємо рядок на числа за допомогою split і перетворюємо на ціле число
            numbers = [int(x) for x in item.split(',')]
            result.append(sum(numbers))  # Додаємо суму чисел у результат
        except AttributeError:
            # Якщо елемент не є рядком, додаємо повідомлення про помилку
            result.append("Не можу це зробити! AttributeError")
        except ValueError:
            # Якщо не можна перетворити на числа, додаємо повідомлення про помилку
            result.append("Не можу це зробити!")
    return result

if __name__ == "__main__":
    print(sum_numbers_in_list(["1,2,3", "4,0,6"]))
    print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))
    print(sum_numbers_in_list(["1,2,3,4", 7]))
    print(sum_numbers_in_list([]))
    print(sum_numbers_in_list("21"))
    print("\nEnd")
