# 1. Обробка файлу `login.xml`

# 1. Створіть функцію знаходження hmdtoken 
# 2. Функція повинна повернути значення дочірнього елемента n:expires     
# 3. Результат виведіть у консоль 

import xml.etree.ElementTree as ET
from pathlib import Path

def get_hmdtoken_nexpires(filepath: Path):
    tree = ET.parse(filepath)
    root = tree.getroot()
    expires_element = root.find(".//{*}expires")
    if expires_element is not None:
        return expires_element.text
    else:
        return "Елемент expires не знайдено"

if __name__ == "__main__":
    xml_path = Path(__file__).parent / "login.xml"
    result = get_hmdtoken_nexpires(xml_path)   
    print(f"Task 1. Обробка файлу `login.xml`. Значення n:expires: {result}")
   

# 2. Обробка файлу `groups.xml`
# 1. Створіть функцію пошуку по group/number 
# 2. Функція повинна повернути значення timingExbytes/incoming 
# 3. Результат виведіть у консоль

def get_timingExbytes_incoming(filepath: Path):
    tree = ET.parse(filepath)
    root = tree.getroot()
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
           incoming = timing_exbytes.find('incoming') 
           if incoming is not None:
               return incoming.text
           else:
               print("Значення timingExbytes/incoming не знайдено")
if __name__ == "__main__":
    xml_path = Path(__file__).parent / "groups.xml"
    result = get_timingExbytes_incoming(xml_path)   
    print(f"Task 2. Обробка файлу `groups.xml`. Значення timingExbytes/incoming: {result}")