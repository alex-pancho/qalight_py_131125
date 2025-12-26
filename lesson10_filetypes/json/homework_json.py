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
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
            print("Файл не знайдено.")
    except json.JSONDecodeError as e:
            print("JSON-дані мають неправильний формат і не можуть бути розібрані", e)
        

def write_json(filepath: Path, content:dict) -> bool:
    """
    Записує Python об'єкт у JSON файл.
    
    Args:
        data (dict/list): Дані для запису
        filepath (Path): Шлях до файла для запису
        
    Returns:
        bool: True якщо успішно записано, False в іншому випадку
    """
    try:
        with open(filepath, "w", encoding="utf-8", ) as file:
            json.dump(content, file, indent=4)
            return filepath.exists()
    except Exception as e:
         print(f'Помилка при записі', e)
         return False

if __name__ == "__main__":
    my_dir = Path(__file__).parent
    my_json = Path(__file__).parent / "file_03.json"
    if not my_json.exists:
         write_json(my_json, {"info": "initial data"})
    content = read_json(my_json)
    print(f'Прочитано з файлу:', content, type(content))
    json_string = '{"name": "Ivan", "age": 25, "city": "Kyiv", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'
    json_to = json.loads(json_string)
    print(f'Конвертовано з рядка', json_to)
    new_json = Path(__file__).parent / "new.json"
    if write_json(new_json, json_to):
         print(f'Новий файл успішно створено')
