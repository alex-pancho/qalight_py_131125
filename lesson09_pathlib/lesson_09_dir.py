from pathlib import Path

print(__file__, type(__file__))

file_path = Path(__file__)
print(file_path, type(file_path))
print("path is file", file_path.is_file())
print("path is dir", file_path.is_dir())
print("path exsist", file_path.exists())

current_dir = file_path.parent
print(current_dir)
project_dir = file_path.parent.parent
print(project_dir)

all_dirs = [d for d in project_dir.iterdir() if d.is_dir()]
print(all_dirs)
all_files = [d for d in project_dir.iterdir() if d.is_file()]
print(all_files)
extension = ".md"
files_with_extension = [f for f in project_dir.iterdir() if f.suffix == extension]
print(files_with_extension)

lesson_08_path = project_dir / "lesson08_try_except"
all_files_12 = [d for d in lesson_08_path.iterdir() if d.is_file()]
print(all_files_12)

current_work_directory = Path.cwd()
print("Поточна робоча директорія:", current_work_directory)

home_dir = Path.home()
print("Домашня директорія користувача:", home_dir)

new_dir = current_work_directory / "directory" / "subdir"
new_dir.mkdir(parents=True, exist_ok=True)
print(new_dir.is_dir())
