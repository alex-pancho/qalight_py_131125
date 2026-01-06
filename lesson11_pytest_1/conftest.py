import pytest
import csv
from pathlib import Path

curr_dir = Path(__file__).parent

@pytest.fixture
def default_user():
    # Підготовка даних
    user = {"name": "Ivan", "role": "admin", "balance": 100}
    return user


def read_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        r = []
        for item in rows:
            r.append((int(item[0]), item[1].strip()!="False"))
        return r

def get_data():
    file = curr_dir / "data.csv"
    rows = read_csv(file)
    return rows


if __name__ == "__main__":
    file = curr_dir / "data.csv"
    rows = read_csv(file) 
    print(rows)
