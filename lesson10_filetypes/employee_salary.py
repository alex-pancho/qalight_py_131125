# Список містить словники - дані співробітників фірми (прізвище, зарплата і стать).
# Скласти функцію, яка повертає тапл: а) прізвище особи, яка має найбільшу
# зарплату (якщо більше одного - перше по алфавіту); б) розмір найменшої зарплати чоловіків, в) розмір найвищої зарплати жінок
salary_list = [
  {"name": "Azimova", "salary": 20000, "gender": "f"},
  {"name": "Borenko", "salary": 9000, "gender": "m"},
  {"name": "Vasilenko", "salary": 10000, "gender": "m"},
  {"name": "Zabolotna", "salary": 25000, "gender": "f"},
  {"name": "Koval", "salary": 35000, "gender": "m"},
]
def salary_surname(salary_list):
    # початкові значення
    max_salary = 0
    max_names = []
    min_salary_men = None
    max_salary_women = None

    for item in salary_list:
        name = item["name"]
        salary = item["salary"]
        gender = item["gender"]

        if salary > max_salary:
            max_salary = salary
            max_names = [name]
        elif salary == max_salary:
            max_names.append(name)

        if gender == "m":
            if min_salary_men is None or salary < min_salary_men:
                min_salary_men = salary

        if gender == "f":
            if max_salary_women is None or salary > max_salary_women:
                max_salary_women = salary

    max_names.sort()
    max_name = max_names[0]
    return max_name, min_salary_men, max_salary_women

print(salary_surname(salary_list))
