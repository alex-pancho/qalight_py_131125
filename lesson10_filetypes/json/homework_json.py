import json
from pathlib import Path

def read_json(filepath: Path) -> dict:
    """
    Читає JSON файл та повертає його вміст як Python об'єкт.

    Args:
        filepath (Path): Шлях до JSON файла

    Returns:
        dict/list: Вміст JSON файла

    Raises:
        FileNotFoundError: Якщо файл не знайдено
        json.JSONDecodeError: Якщо файл містить невалідний JSON
    """
    with open(filepath, "r", encoding="utf-8") as file:
        # Ваш код тут
        content = json.load(file)
        return content

def write_json(filepath: Path, content: dict):
    """
    Записує Python об'єкт у JSON файл.

    Args:
        data (dict/list): Дані для запису
        filepath (Path): Шлях до файла для запису

    Returns:
        bool: True якщо успішно записано, False в іншому випадку
    """
    with open(filepath, "w", encoding="utf-8", ) as file:
        json.dump(content, file, indent=4)
        # Ваш код тут
        return True

if __name__ == "__main__":
    my_json = Path(__file__).parent / "test_result.json"
    content = read_json(my_json)
    print(content, type(content))
    json_string = '{"name": "Ivan", "age": 25, "city": "Kyiv", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'
    json_to = json.loads(json_string)
    print(json_to)
    new_json = Path(__file__).parent / "new.json"
    write_json(new_json, json_to)

#------------------------------------------------------------------------------------
# # Валідація JSON
# Ваше завдання полягає в тому, щоб перевірити JSON-файли на коректність та вивести повідомлення про помилки, якщо вони є.
#
# Приблизний алгоритм:
# 1. Прочитайте JSON-файли "file_01.json", "file_02.json", "file_03.json".
# 2. Використовуйте модуль `json` для валідації JSON.
# 3. Якщо JSON некоректний, виведіть повідомлення про помилку.

def validate_json(filepath: Path):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            json.load(file)
        print(f"Файл {filepath.name} — коректний JSON")
    except FileNotFoundError:
        print(f"Файл {filepath.name} не знайдено")
    except json.JSONDecodeError as error:
        print(f"Помилка в JSON-файлі {filepath.name}")
        print(f"Рядок {error.lineno}, позиція {error.colno}")
        print(f"Повідомлення: {error.msg}")

if __name__ == "__main__":
    base_path = Path(__file__).parent

    files = [
        base_path / "file_01.json",
        base_path / "file_02.json",
        base_path / "file_03.json"
    ]
    for file in files:
        validate_json(file)
