# Lesson 04 — Functions & Exceptions

**Day 4** · Notebook: [`functions_and_exceptions.ipynb`](functions_and_exceptions.ipynb)

Packaging logic into reusable functions, and handling errors. Opens with a revision of Lesson 03.

## Topics

- Defining and calling functions
- Parameters, multiple parameters, default parameters
- `return` — including returning multiple values
- Global vs. local variables
- `*args` — unknown number of positional arguments
- `**kwargs` — unknown number of keyword arguments
- Type hints
- Docstrings
- Exception handling with `try` / `except`

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_basic_functions.py`](examples/01_basic_functions.py) | Parameters, `return`, returning several values |
| [`02_arguments.py`](examples/02_arguments.py) | Positional/keyword/default args + the mutable-default trap |
| [`03_args_kwargs.py`](examples/03_args_kwargs.py) | `*args`, `**kwargs`, and unpacking with `*`/`**` |
| [`04_scope.py`](examples/04_scope.py) | Local vs. global, and why to avoid `global` |
| [`05_type_hints_and_docstrings.py`](examples/05_type_hints_and_docstrings.py) | Google-style docstrings, `help()`, type hints |
| [`06_exception_handling.py`](examples/06_exception_handling.py) | `try`/`except`/`else`/`finally`, `raise` |
| [`07_exercises_solved.py`](examples/07_exercises_solved.py) | Exercise solutions |

## Exercises

1. Write a `greet()` function.
2. Reverse the words in a sentence using a function.
3. Return the largest number in a list — with and without `max()`.
4. Student grade calculator built from functions.

## Prerequisites

[Lesson 03 — Data Structures](../03-data-structures/)

## Next

[Lesson 05 — OOP: Classes & Objects](../05-oop-classes-and-objects/)
