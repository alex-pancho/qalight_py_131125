# Пошук дублікатів у CSV
# Ваше завдання полягає в тому, щоб знайти дублікатні рядки у CSV-файлах.

# Приблизний алгоритм:
# 1. Прочитайте CSV-файли "users_1.csv" (Total records: 260), "users_1.csv" (Total records: 260).
# 2. Зберігайте кожен рядок у множині або словнику для виявлення дублікатів.
# 3. Якщо рядок вже існує у множині/словнику, це дублікат, його слід пропустити
# 4. Виведіть або збережіть оригінальні рядки у окремий файл "clean_users_3.csv"

import csv
from pathlib import Path

def get_data_from_csv(filepath : Path):
    rows = []
    with open(filepath, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            rows.append(row)
    return headers, rows

def filter_unique_data(all_rows):
    unique_rows = set()
    clean_data = []
    for row in all_rows:
        row_tuple = tuple(row.values())
        if row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            clean_data.append(row)
    return clean_data
        
if __name__ == "__main__":
    my_dir = Path(__file__).parent 

    headers_1, data_1 = get_data_from_csv(my_dir / "users_1.csv")
    headers_2, data_2 = get_data_from_csv(my_dir / "users_2.csv")

    combined_data = data_1 + data_2
    print(f'Загальна кількість записів в обох файлах до виявлення дублікатів:', {len(combined_data)})

    final_data = filter_unique_data(combined_data)
    print(f'Загальна кількість записів після виявлення дублікатів:', {len(final_data)})

    output_path = my_dir / "clean_users_3.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers_1)
        writer.writeheader()
        writer.writerows(final_data)
    print(f'Оригінальні рядки збережені у окремий файл', {output_path.name})

