import json
from pathlib import Path


def read_json(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    base_path = Path(__file__).parent

    files = [
        base_path / "file_01.json",
        base_path / "file_02.json",
        base_path / "file_03.json",
    ]

    results = []

    for file in files:
        try:
            read_json(file)
            results.append(f"{file.name}: OK")
        except json.JSONDecodeError as e:
            results.append(f"{file.name}: JSON error ({e})")
        except FileNotFoundError:
            results.append(f"{file.name}: file not found")

    print("\n".join(results))
