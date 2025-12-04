# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
set_from_small_list = set(small_list)
print(f'Task 1. Унікальними елементами в списку small_list є: {set_from_small_list}')

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = sum(small_list) / len(small_list)
print(f'Task 2. Середнє арифметичне всіх елементів у списку small_list становить {average}')

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
big_set = set(big_list)
if len(big_list) > len(big_set):
    print("Task 3. В списку big_list є дублікати")
else:
    print("Task 3. В списку big_list немає дублікатів")

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key = max(add_dict, key = add_dict.get)
print(f'Task 4. Ключом з максимальним значенням у словнику add_dict є: {max_key}')

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
new_base_dict = base_dict.copy()
reverse_dict = {value: key for key, value in new_base_dict.items()}
print(f'Task 5. Новий словник, в якому ключі та значення зі словника base_dict замінені місцями: {reverse_dict}')

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        str_base = str(sum_dict[key])
        str_add = str(value)
        sum_dict[key] = str_base + str_add
    else:
        sum_dict[key] = value
print(f'Task 6. Новий словник sum_dict: {sum_dict}')

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_from_line = set(line)
print(f'Task 7. Множина всіх символів, які входять у заданий рядок: {set_from_line}')

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
symmetric_difference = set_1 ^ set_2
sum_of_elements = sum(symmetric_difference)
print(f'Task 8. Сума елементів двох множин, які не є спільними: {sum_of_elements}')

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
first_list = [1, 2, 3, 22, 46, 78, 52, 88, 99, 101, 7, 9, 13]
second_list = [46, 88, 101, 13, 3, 5, 17, 66, 47, 83, 222, 333, 56, 94]
first_set = set(first_list)
second_set = set(second_list)
symmetric_difference_set = first_set ^ second_set
print(f'Task 9. Сет, який містить всі елементи з обох списків, які зустрічаються тільки один раз: {symmetric_difference_set}')

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_dict = {'10-19':[], '20-29':[], '30-39':[], '40-49':[]}

for person in person_list:
    if person[1] in range(10, 20):
        person_dict['10-19'].append(person[0]) 
    if person[1] in range(20, 30):
        person_dict['20-29'].append(person[0])
    if person[1] in range(30, 40):
        person_dict['30-39'].append(person[0])
    if person[1] in range(40, 50):
        person_dict['40-49'].append(person[0])
print(f'Task 10. Cловник, де ключі - вікові діапазони, а значення - списки імен людей, які потрапляють в кожен діапазон: {person_dict}')