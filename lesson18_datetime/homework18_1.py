'''Засобами автоматизації проаналізуйте наданий нам лог: 
[heartbeat\hblog](https://github.com/alex-pancho/testing_ideas/blob/main/heartbeat/hblog)

Змініть заготовку - файл hb_proces.py так щоб був аналіз правилності вимог:
    для кожного випадку де heartbeat більше 31 сек але менше рівно 33 логувало WARNING в файл hb_test.log
    для кожного випадку де heartbeat більше  33 логувало ERROR в файл hb_test.log'''

import datetime
import logging

logging.basicConfig(
    filename='hb_test_1.log',
    filemode='w',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)
def process_heartbeats(filepath):
    timestampts = []

    with open(filepath, 'r') as f:
        for line in f:
            if "Timestamp" in line:
                parts = line.split()
                time_str = parts[10]

                dt = datetime.datetime.strptime(time_str, '%H:%M:%S')
                if not timestampts or timestampts[-1] != dt:
                    timestampts.append(dt)
    timestampts.reverse()    # розвертаємо для зручності читання подій з початку відстеження серцебиття, в принципі можна цього не робити

    for i in range(1, len(timestampts)):
        diff = (timestampts[i] - timestampts[i - 1]).total_seconds()
        if 31 < diff <= 33:
            logging.warning(f"Heartbeat interval is {diff} seconds between {timestampts[i - 1].strftime('%H:%M:%S')} and {timestampts[i].strftime('%H:%M:%S')}")
        if diff > 33:
            logging.error(f"Heartbeat interval is {diff} seconds between {timestampts[i - 1].strftime('%H:%M:%S')} and {timestampts[i].strftime('%H:%M:%S')}")

if __name__ == "__main__":
    process_heartbeats("hblog.txt")
    print("Analisys completed")