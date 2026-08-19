# Lesson 07 — File Handling

**Day 7** · Notebooks:
1. [`01_file_basics.ipynb`](01_file_basics.ipynb) — functions revision, then opening and reading a file
2. [`02_read_write_and_json.ipynb`](02_read_write_and_json.ipynb) — the full read/write/append/JSON tour

Reading and writing files so data survives after the program exits.

## Topics

- `open(filepath, mode)` and file modes: `r`, `w`, `a`, `x`, `rb`, `wb`, `r+`, `w+`
- Reading: `read()`, `read(n)`, `readline()`, `readlines()`, looping over a file object
- Writing and appending
- Creating a new file with `x` mode
- `close()` and the `with` statement
- The `os` module — `os.path.exists()`, `os.path.getsize()`, `os.getcwd()`, `os.listdir()`,
  `os.mkdir()`, `os.remove()`
- JSON files — `json.load()` and `json.dump()`

## Sample Data

| File | Used by |
| ---- | ------- |
| [`student.txt`](student.txt) | both notebooks — plain-text reading and writing |
| [`student.json`](student.json) | notebook 2 — loading, appending a record, saving back |

> The notebooks use paths relative to this folder, and some cells **overwrite**
> `student.txt` or create/delete `fruits.txt`. That is intentional — restore them with
> `git checkout` if you want to start over.

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_reading_files.py`](examples/01_reading_files.py) | `read`, `read(n)`, `readline`, `readlines`, looping |
| [`02_writing_and_modes.py`](examples/02_writing_and_modes.py) | `w` vs `a` vs `x`, `FileNotFoundError` |
| [`03_with_statement.py`](examples/03_with_statement.py) | Why `with` beats manual `close()` |
| [`04_json_files.py`](examples/04_json_files.py) | `load`/`dump` vs `loads`/`dumps`, JSON↔Python types |
| [`05_csv_files.py`](examples/05_csv_files.py) | `csv.reader`, `DictReader`, `DictWriter` |
| [`06_paths_with_os_and_pathlib.py`](examples/06_paths_with_os_and_pathlib.py) | `os.path` and the modern `pathlib` |
| [`07_diary_app.py`](examples/07_diary_app.py) | Exercise solution — interactive, uses real `input()` |

## Exercises

1. Personal diary — a menu-driven program (write / read / exit) storing entries in `diary.txt`.
2. Load `student.json`, add a new student, and write the file back out.

## Prerequisites

[Lesson 04 — Functions & Exceptions](../04-functions/)

## Next

[Lesson 08 — Modules & Packages](../08-modules-and-packages/)
