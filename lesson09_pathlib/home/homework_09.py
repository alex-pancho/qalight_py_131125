### Робота з файлами та папками — завдання
from pathlib import Path
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here

def process_file(filepath: Path, text_1: str, text_2: str):
    # 1. Створення і запис
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text_1)
    print(f"1. Створення і запис файлу {filepath.name}: {text_1}")
    # 2. Читання файлу
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"2. Читання файлу {filepath.name}: {content}")
    # 3. Допис у файл
    with open(filepath, "a", encoding="utf-8") as file:
        file.write("\n" + text_2)
    print(f"3. Допис файлу {filepath.name}: {text_2}")
    # 4. Читання кількох рядків
    print(f"4. Читання кількох рядків з {filepath.name}:")
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
    # 5. Підрахунок символів
    with open(filepath, "r", encoding="utf-8") as file:
        total_chars = len(file.read())
    print(f"5. Кількість символів у {filepath.name}: {total_chars}")
def create_folder_and_file(folder: Path, file_text: dict):
    # 6. Створюємо папку, якщо її немає
    folder.mkdir(exist_ok=True)
    print(f"6. Створення папки \"{folder.name}\"")
    # 6. Створення файлів і записуємо текст
    for filename, text in file_text.items():
        file_path = folder / filename
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"6.{filename} Створення і запис файлу {filename}: {text}")
    # 7. Виводимо список всіх файлів у папці
    print(f"7. Список файлів у папці {folder.name}:")
    for item in folder.iterdir():
        if item.is_file():
            print(item.name)
    return folder
def copy_file (notes_path1: Path, notes_path2: Path):
    # 8. Читаємо файл і створюємо копіювання з файлу
    with open(notes_path1, "r", encoding="utf-8") as file:
        content = file.read()
    with open(notes_path2, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"8. Копіювання {notes_path1.name} -> {notes_path2.name}: {content}")
def create_files(a_txt: Path, b_txt: Path, ab_txt: Path, text_a: str, text_b: str):
    # 9.1. Створюємо файл a.txt і записуємо текст
    with open(a_txt, "w", encoding="utf-8") as file:
        file.write(text_a)
    print(f"9.1. Створення і запис файлу {a_txt.name}: {text_a}")
    # 9.2. Створюємо файл b.txt і записуємо текст
    with open(b_txt, "w", encoding="utf-8") as file:
        file.write(text_b)
    print(f"9.2. Створення і запис файлу {b_txt.name}: {text_b}")
    # 9.3. Читаємо обидва файли
    with open(a_txt, "r", encoding="utf-8") as file:
        content_a = file.read()
    with open(b_txt, "r", encoding="utf-8") as file:
        content_b = file.read()
    # 9.4. Створюємо файл ab.txt і записуємо об'єднаний текст
    with open(ab_txt, "w", encoding="utf-8") as file:
        file.write(content_a + content_b)
    print(f"9.4. Об'єднання файлів у {ab_txt.name}: {content_a + content_b}")
def find_word(filepath: Path, word: str):
    # 10. Пошук слова у файлі
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
    print(f"10. Читання файлу {filepath.name}: {text}")
    if word in text:
        print(f"Слово \"{word}\" знайдено у {filepath.name}")
    else:
        print(f"Слово \"{word}\" не знайдено у {filepath.name}")


process_file(Path("hello.txt"), "Hello, Python!", "Learning file operations.")
data = create_folder_and_file(Path("data"),
                                     {"notes_1.txt": "My first note.", "notes_2.txt": "My second note."})
copy_file(data / "notes_1.txt", data / "copy.txt")
create_files(Path("a.txt"), Path("b.txt"), Path("ab.txt"), "Text A\n", "Text B\n")
find_word(data / "notes_1.txt", "note")

