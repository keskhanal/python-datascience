# Lesson 01 — Python Basics

**Day 1** · Notebook: [`python_basics.ipynb`](python_basics.ipynb)

The first hour of Python: printing, reading input, storing values, and doing arithmetic.

## Topics

- Comments — single-line and multi-line
- `print()` and `input()`
- Variables and naming conventions (snake_case, valid names)
- Data types: `int`, `float`, `str`, `bool`
- Type conversion (`int()`, `float()`, `str()`) and why `input()` always returns a string
- f-strings
- Operators
  - Arithmetic: `+`, `-`, `*`, `**`, `/`, `//`, `%`
  - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - Logical: `and`, `or`, `not`

## Examples

Runnable scripts in [`examples/`](examples/) — run any of them with `python examples/<file>`.

| Script | Shows |
| ------ | ----- |
| [`01_variables_and_types.py`](examples/01_variables_and_types.py) | `int`/`float`/`str`/`bool`, `type()`, naming rules |
| [`02_fstrings.py`](examples/02_fstrings.py) | f-strings, rounding, aligning output |
| [`03_type_conversion.py`](examples/03_type_conversion.py) | Why `input()` needs `int()`, and conversions that fail |
| [`04_operators.py`](examples/04_operators.py) | All the operator families side by side |
| [`05_temperature_converter.py`](examples/05_temperature_converter.py) | Exercise solution |

## Exercises

1. Print your name and a sentence about your city.
2. Read a name from the user and greet them with an f-string.
3. Read an age and print `My age is 50 years old.`
4. Read two numbers and print their sum, difference, product, and quotient.
5. Convert 97 °F to Celsius using `c = (f - 32) * (5/9)`.

## Next

[Lesson 02 — Control Flow](../02-control-flow/)
