# Валідація JSON
# Ваше завдання полягає в тому, щоб перевірити JSON-файли на коректність та вивести повідомлення про помилки, 
# якщо вони є.

# Приблизний алгоритм:
# 1. Прочитайте JSON-файли "file_01.json", "file_02.json", "file_03.json".
# 2. Використовуйте модуль `json` для валідації JSON.
# 3. Якщо JSON некоректний, виведіть повідомлення про помилку.

import json
from pathlib import Path

def read_json(filepath : Path):
    try:
        # читаємо JSON-файли
        with open (filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f'Читаємо JSON-файл: {filepath.name}')
            print(data)
    
        # виводимо повідомлення про помилку, якщо JSON некоректний (знаємо що File_02 дає JSONDecodeError)
    except json.JSONDecodeError as e:
        print(f'{filepath.name}, Помилка розбору JSON:', e)

        # виводимо повідомлення про відсутність необхідних прав доступу
    except PermissionError:
        print(f'{filepath.name}, Немає прав доступу до файлу')

        # виводимо повідомлення про те, що файл не знайдено. 
        # Для валідації помилки додано шлях до неіснуючого файла file_04.json
    except FileNotFoundError:
        print(f'{filepath.name}, Файл не знайдено')

if __name__ == "__main__":
    my_dir = Path(__file__).parent

    # оптимізуємо код за порадою Gemini, робимо список файлів для перевірки, 
    # щоб не визначати файли 4 рази і не запускати 4 функції
    json_files = ["file_01.json", "file_02.json", "file_03.json", "file_04.json"]
    for filename in json_files:
        read_json(my_dir / filename)