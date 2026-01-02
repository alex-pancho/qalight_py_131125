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

def process_file(filepath: Path):
    # 1. Створення і запис
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("Hello, Python!")
    print("1.Створення і запис файлу:", "Hello, Python!")
    # 2. Читання файлу
    with open(filepath, "r", encoding="utf-8") as file:
        print("2.Читання файлу:", file.read())
    # 3. Допис файлу
    with open(filepath, "a", encoding="utf-8") as file:
        file.write("\nLearning file operations.")
    print("3.Допис файлу:", "Learning file operations.")
    # 4. Читання кількох рядків
    print("4.Читання кількох рядків:")
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
    # 5. Підрахунок символів
    with open(filepath, "r", encoding="utf-8") as file:
        print("5: Кількість символів:", len(file.read()))

def create_folder_and_file(folder: Path):
    # 6. Створюємо папку, якщо її немає
    folder.mkdir(exist_ok=True)
    print("6. Створення папки \"data\"")
    # 6. Створюємо notes.txt і записуємо текст
    notes_path1 = folder / "notes_1.txt"
    with open(notes_path1, "w", encoding="utf-8") as file:
        file.write("My first note.")
    print("6.1. Створення і запис першого файлу:", "My first note.")
    # 6.1 Створюємо notes2.txt і записуємо текст
    notes_path2 = folder / "notes_2.txt"
    with open(notes_path2, "w", encoding="utf-8") as file:
        file.write("My second note.")
    print("6.2. Створення і запис другого файлу:", "My second note.")
    # 7. Виводимо список всіх файлів у папці
    print("7. Список файлів у папці:")
    for item in folder.iterdir():
        print(item.name)
    # 8. Читаємо notes.txt
    with open(notes_path1, "r", encoding="utf-8") as file:
        content = file.read()
    print("8. Читання файлу:", content)
    # 9. Створюємо copy.txt і записуємо в нього вміст notes.txt
    copy_path = folder / "copy.txt"
    with open(copy_path, "w", encoding="utf-8") as file:
        file.write(content)
    print("8.1. Створено copy.txt з вмістом notes_1.txt:", content)

def create_files(a_txt: Path, b_txt: Path, ab_txt: Path):
    # 9.1. Створюємо файл a.txt і записуємо текст
    with open(a_txt, "w", encoding="utf-8") as file:
        file.write("Text A\n")
    print("9.1. Створення і запис файлу a.txt: Text A")
    # 9.2. Створюємо файл b.txt і записуємо текст
    with open(b_txt, "w", encoding="utf-8") as file:
        file.write("Text B\n")
    print("9.2. Створення і запис файлу b.txt: Text B")
    # 9.3. Читаємо файл a.txt
    with open(a_txt, "r", encoding="utf-8") as file:
        content_a = file.read()
    print("9.3. Читання файлу a.txt:", content_a.strip())
    # 9.4. Читаємо файл b.txt
    with open(b_txt, "r", encoding="utf-8") as file:
        content_b = file.read()
    print("9.4. Читання файлу b.txt:", content_b.strip())
    # 9.5. Створюємо файл ab.txt і записуємо об'єднаний текст
    content_ab = content_a + content_b
    with open(ab_txt, "w", encoding="utf-8") as file:
        file.write(content_ab)
    print("9.5. Створення файлу ab.txt:", content_ab)

def find_word():
    # 10. Пошук слова у файлі
    with open("data/notes_1.txt", "r", encoding="utf-8") as file:
        text = file.read()
        print("10.Читання файлу:", text)
    if "note" in text:
        print("Слово \"note\" у тексті знайдено")
    else:
        print("Слово \"note\" у тексті не знайдено")


process_file(Path("hello.txt"))
create_folder_and_file(Path("data"))
create_files(Path("a.txt"), Path("b.txt"), Path("ab.txt"))
find_word()

