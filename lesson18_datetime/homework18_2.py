'''Необовязова частина, виклик для найтриваліших:
(на оцінку не впливає, на самоцінку - впливає)
Врахуйте, що моніторінгових процесів декілька і вони ідентифікуються по ключу наприклад:

    Key TSTFEED0300
    Key TSTFEED0240

це два різні процеси, відповідно, для пошуку наступного"удару" слід також враховувати ключ.
Подумайте, що завтра вам використовувати файл hb_proces.py для тестів багатьох файлів
Згадайте, що ми вчили про серіалізацію і генератори, може воно тут треба.
(а може ні і я вас залутую) (а може базу даних в пам'яті ???)
'''
import datetime
import logging
import os

logging.basicConfig(
    filename='hb_test_2.log',
    filemode='w',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)
def log_reader(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found!")
        return
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in reversed(lines):
            if "Timestamp" in line and "Key" in line:
                parts = line.split()
                try:
                    time_str = parts[10]
                    key_str = parts[12]
                    yield {
                        "timestampt" : datetime.datetime.strptime(time_str, '%H:%M:%S'),
                        "key" : key_str
                    }
                except (ValueError, IndexError):
                    continue
def process_multi_heartbeats(filepath):
    last_heartbeats = {}
    for record in log_reader(filepath):
        key = record["key"]
        current_time = record["timestampt"]
        if key in last_heartbeats:
            previous_time = last_heartbeats[key]
            diff = (current_time - previous_time).total_seconds()
            
            if 31 < diff <= 33:
                logging.warning(f"[{key}] WARNING: interval {diff}s between {previous_time.time()} and {current_time.time()}")
            elif diff > 33:
                logging.error(f"[{key}] ERROR: interval {diff}s between {previous_time.time()} and {current_time.time()}")
    last_heartbeats[key] = current_time

if __name__ == "__main__":
    logging.info("Analisys with Timestampts and Keys started!")
    process_multi_heartbeats("hblog.txt")
    logging.info("Analisys with Timestampts and Keys completed!")
    print("Analisys completed")