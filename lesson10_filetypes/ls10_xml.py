from pathlib import Path
import xml.etree.ElementTree as ET


my_dir = Path(__file__).parent
xml_file = my_dir / "groups.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib, child.text)
    for subchild in child:
        print(subchild.tag, subchild.attrib, subchild.text)

for chapter in root.findall("book/content/chapter"):
    print(chapter.tag, chapter.attrib, chapter.text)