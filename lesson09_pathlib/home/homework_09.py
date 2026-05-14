### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
from pathlib import Path

def create_and_write_input_file(filename = 'hello.txt'):
    current_dir = Path.cwd()
    new_input_file = current_dir / filename

    with open(new_input_file, 'w', encoding='utf-8') as input_file:
        input_file.write('Hello, Python!')
        print(f'Created a new input_file', new_input_file)
create_and_write_input_file()

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
def read_input_file(filename = 'hello.txt'):
    current_dir = Path.cwd()
    new_input_file = current_dir / filename
    with open(new_input_file, 'r', encoding='utf-8') as input_file:
        content = input_file.read()         
        print(content)
read_input_file()

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning input_file operations.
   ```
"""
def append_input_file(filename = 'hello.txt'):
   current_dir = Path.cwd()
   new_input_file = current_dir / filename
   with open(new_input_file, 'a', encoding='utf-8') as input_file:
        input_file.write('\\nLearning input_file operations.')
append_input_file()
read_input_file()

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
def read_all_line_in_input_file(filename = 'hello.txt'):
   current_dir = Path.cwd()
   new_input_file = current_dir / filename
   with open(new_input_file, 'r', encoding='utf-8') as input_file:
         for line in input_file:
            split_line = line.split('\\n')
            print(f'Перший рядок:', split_line[0])
            print(f'Другий рядок:', split_line[1])
            
read_all_line_in_input_file()

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
def count_symbols_in_input_file(filename = 'hello.txt'):
   current_dir = Path.cwd()
   new_input_file = current_dir / filename
   with open(new_input_file, 'r', encoding='utf-8') as input_file:
        content = input_file.read()         
        print(f'У файлі `hello.txt` кількість символів:', len(content))
count_symbols_in_input_file()

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
def create_dir_with_input_file(directory_path: str | Path):
    data_dir = Path(directory_path)
    data_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
    data_input_file = data_dir / 'notes.txt'

    with open(data_input_file, 'w', encoding='utf-8') as input_file:
        input_file.write('My first note.')
        print(f'Created a new directory and data_input_file', data_input_file)
create_dir_with_input_file("C:/GitHub/data")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
def input_file_list(directory_path: str | Path):
   data = Path(directory_path)
   input_files = [f.name for f in data.iterdir() if f.is_file()]
   print(f'У папці {data.name} знаходяться такі файли:', input_files)
input_file_list("C:/GitHub/data")

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
def read_and_copy_input_file(directory : Path, input_file : Path, output_file : Path):    
   with open(directory/input_file, 'r', encoding='utf-8') as input_file:
      content = input_file.read()           
   with open(directory/output_file, 'w', encoding='utf-8') as output_file:
      output_file.write(content)

def check_len_in_files(directory : Path, input_file : Path, output_file : Path):
   with open(directory/input_file, 'r', encoding='utf-8') as input_file:
      content = input_file.read()          
   with open(directory/output_file, 'r', encoding='utf-8') as output_file:
      output_content = output_file.read()  
   if len(content) == len(output_content):
      print("Запис вмісту файлу `notes.txt` в файл `copy.txt` успішний!")
   else:
      print("Щось пішло не так.")

read_and_copy_input_file(directory = Path("C:/GitHub/data"), input_file = 'notes.txt', output_file = 'copy.txt')
check_len_in_files(directory = Path("C:/GitHub/data"), input_file = 'notes.txt', output_file = 'copy.txt')

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
def create_files(directory : Path):
   a_path = directory / 'a.txt'
   b_path = directory / 'b.txt'

   with open(a_path, 'w', encoding='utf-8') as afile:
      afile.write('Який чудовий цей світ!')
   with open(b_path, 'w', encoding='utf-8') as bfile:
      bfile.write('Зупиніть цю Землю, я зійду!')

def write_from_files(directory : Path):
   a_path = directory / 'a.txt'
   b_path = directory / 'b.txt'
   ab_path = directory / 'ab.txt'

   with open (a_path, 'r', encoding='utf-8') as a_file:
      content_1 = a_file.read()
   with open (b_path, 'r', encoding='utf-8') as b_file:
      content_2 = b_file.read()
      union_content = content_1 + " " + content_2
   with open(ab_path, 'w', encoding='utf-8') as ab_file:
      ab_file.write(union_content)
   print(f'Зміст файлів: {a_path.name} і {b_path.name}, записаний у новий файл {ab_path.name}:', union_content)
   
create_files(directory = Path("C:/GitHub/data"))
write_from_files(directory = Path("C:/GitHub/data"))

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
def find_word(directory : Path):
   output_file = directory / 'copy.txt'

   with open(output_file, 'r', encoding='utf-8') as file_for_finding:
      content = file_for_finding.read()
      if "note" in content:
         print("Знайдено")
      else:
         print("Не знайдено")
find_word(directory = Path("C:/GitHub/data"))


