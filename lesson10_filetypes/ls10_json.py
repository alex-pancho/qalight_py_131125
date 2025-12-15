import json
from pathlib import Path


my_dir = Path(__file__).parent
load_file = my_dir / "login.json"

def read_json(load_file: Path) -> dict | None:
    """
    Docstring for read_json
    
    :param load_file: path for file
    :type load_file: Path
    """
    with load_file.open(encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = None
    return data

print(read_json(load_file))

data_to_json = {
    "name": "Oleksandra",
    "learn_year": 2025,
    "is_finished": False,
    "link_to_cert": None,
    "name2": {"name": "Oleksandra",
    "learn_year2": 2025,
    "is_finished2": False,
    "link_to_cert2": None,}
}

output_file = my_dir / "out.json"
# f = output_file.open("w", encoding="utf-8")
def write_json(output_file: Path, data_to_json: dict | list):
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data_to_json, f, indent=2)

#print(write_json(output_file, data_to_json))
swagger_file = my_dir / "swagger.json"
swager_dict = read_json(swagger_file)
swagger_out_file = my_dir / "swagger_pp.json"
write_json(swagger_out_file, swager_dict)
