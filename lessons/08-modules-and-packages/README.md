# Lesson 08 — Modules & Packages

**Notebook:** [`modules.ipynb`](modules.ipynb)

Splitting code across files, and using Python's standard library.

## Topics

- `import module`, `from module import name`
- Built-in modules — `math`, `datetime`, `random`
- Writing your own module (`maths.py`)
- Turning a folder into a package with `__init__.py`
- `if __name__ == "__main__":`

## Files in This Lesson

| Path | What it shows |
| ---- | ------------- |
| [`maths.py`](maths.py) | A user-defined **module** — `sum_two_numbers`, `multiply_two_numbers`, `divide_two_numbers` |
| [`calculator/`](calculator/) | A **package** whose `__init__.py` re-exports `Calculator` and `greeting` |
| [`student/`](student/) | A package containing the `Student` class |
| [`app.py`](app.py) | Runs the `calculator` package |
| [`main.py`](main.py) | Runs the `student` package |

Run the scripts from this folder so the imports resolve:

```bash
cd lessons/08-modules-and-packages
python app.py
python main.py
python maths.py
```

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_import_styles.py`](examples/01_import_styles.py) | Every import form, and `__name__` |
| [`02_math_module.py`](examples/02_math_module.py) | `math` plus a peek at `statistics` |
| [`03_datetime_module.py`](examples/03_datetime_module.py) | `strftime`/`strptime`, `timedelta`, age calculator |
| [`04_random_module.py`](examples/04_random_module.py) | `randint`, `choice`, `sample`, `shuffle`, `seed` |
| [`05_useful_stdlib.py`](examples/05_useful_stdlib.py) | `collections`, `itertools`, `os`, `sys`, `time` |

Run these from the lesson folder so the local modules resolve:

```bash
cd lessons/08-modules-and-packages
python examples/01_import_styles.py
```

## Exercises

1. Use `datetime` to print today's weekday.
2. Build an age calculator from a date of birth.
3. Use `random.choice()` to pick a student at random from a class list.

## Prerequisites

[Lesson 05 — OOP: Classes & Objects](../05-oop-classes-and-objects/)

## Next

[Lesson 09 — Advanced Python](../09-advanced-python/)
