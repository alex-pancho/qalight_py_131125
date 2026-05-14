# # 1. Обробка файлу `login.xml`
#
# 1. Створіть функцію знаходження hmdtoken
# 2. Функція повинна повернути значення дочірнього елемента n:expires
# 3. Результат виведіть у консоль
#
# # 2. Обробка файлу `groups.xml`
#
# 1. Створіть функцію пошуку по group/number
# 2. Функція повинна повернути значення timingExbytes/incoming
# 3. Результат виведіть у консоль

import xml.etree.ElementTree as ET
from pathlib import Path


# 1. Обробка файлу login.xml
def hmdtoken(filepath: Path) -> str:
    tree = ET.parse(filepath)
    root = tree.getroot()

    ns = {"n": root.tag.split("}")[0].strip("{")}

    for token in root.findall(".//n:hmdtoken", ns):
        expires = token.find("n:expires", ns)  # саме n:expires
        if expires is not None:
            return expires.text

    return "expires не знайдено"

# 2. Обробка файлу groups.xml
def find_group_number(filepath: Path, group_number: str) -> str:
    tree = ET.parse(filepath)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == group_number:
            timing_exbytes = group.find("timingExbytes")
            if timing_exbytes is not None:
                incoming = timing_exbytes.find("incoming")
                if incoming is not None:
                    return incoming.text

    return "incoming не знайдено"

if __name__ == "__main__":
    login_xml = Path("login.xml")
    print("Expires:", hmdtoken(login_xml))

    groups_xml = Path("groups.xml")
    print("Incoming:", find_group_number(groups_xml, "101"))


