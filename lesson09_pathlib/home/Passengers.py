# Задано дані (список списків) про багаж (кількість речей і загальна вага багажу) пасажирів.
# Скласти функцію, яка повертає тапл де міститься:
# а) кількість пасажирів, які мають більше двох речей;
# б) чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг;
# в) число пасажирів, кількість речей яких перевершує середнє число речей всіх пасажирів.

passengers = [
    {'number_of_items': 3, 'total_weight': 30},
    {'number_of_items': 2, 'total_weight': 20},
    {'number_of_items': 1, 'total_weight': 15},
    {'number_of_items': 4, 'total_weight': 40},
]
def baggage_passengers(passengers):
    # 1. Пасажири з більше ніж 2 речами
    pass_two_baggage = 0
    for p in passengers:
        if p['number_of_items'] > 2:
            pass_two_baggage += 1
    print("\nКількість пасажирів з більше ніж 2 речами:", pass_two_baggage)
    # 2. Пасажир з 1 річчю вагою < 25 кг
    pass_one_baggage = False
    for p in passengers:
        if p['number_of_items'] == 1 and p['total_weight'] < 25:
            pass_one_baggage = True
            break
    print("\nЧи є пасажир з 1 річчю <25 кг:", pass_one_baggage)
    # 3. Середня кількість речей
    total_baggage = 0
    for p in passengers:
        total_baggage += p['number_of_items']
    average_items = total_baggage / len(passengers)
    print("\nСередня кількість речей:", average_items)
   # 4. Пасажири з кількістю речей більше середньої
    pass_average = 0
    for p in passengers:
        if p['number_of_items'] > average_items:
            pass_average += 1
    print("\nКількість пасажирів з речами більше середнього:", pass_average)
    # 5. Результат
    result = (pass_two_baggage, pass_one_baggage, pass_average)
    return result
# Фінальний звіт
result_fin = baggage_passengers(passengers)
print("\nФінальний результат (tuple):", result_fin)
