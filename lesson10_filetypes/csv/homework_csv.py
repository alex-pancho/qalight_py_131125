import csv
from pathlib import Path


def read_csv(filepath: Path) -> list[list[str]]:
    with open(filepath, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv(filepath: Path, rows: list[list[str]]) -> None:
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def remove_duplicates(rows: list[list[str]]) -> list[list[str]]:
    seen = set()
    unique_rows = []

    for row in rows:
        row_tuple = tuple(row)  # список → кортеж (для set)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)

    return unique_rows


if __name__ == "__main__":
    base_path = Path(__file__).parent

    file_1 = base_path / "users_1.csv"
    file_2 = base_path / "users_2.csv"
    output_file = base_path / "clean_users_3.csv"

    rows_1 = read_csv(file_1)
    rows_2 = read_csv(file_2)

    all_rows = rows_1 + rows_2
    clean_rows = remove_duplicates(all_rows)

    write_csv(output_file, clean_rows)

    print(f"Було рядків: {len(all_rows)}")
    print(f"Після очищення: {len(clean_rows)}")