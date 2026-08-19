# Lesson 09 — Advanced Python

**Notebook:** [`advanced_python.ipynb`](advanced_python.ipynb)

The idiomatic Python that turns up constantly in data work.

## Topics

- `*args` vs. `**kwargs` (revision, in depth)
- `lambda` functions
- List comprehensions
- `map()`, `filter()`, `sorted()` — including `key=lambda ...`
- Iterators vs. generators — `yield` and lazy evaluation
- Decorators

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_lambda.py`](examples/01_lambda.py) | Lambdas as `key=` arguments, and their limits |
| [`02_comprehensions.py`](examples/02_comprehensions.py) | List/dict/set comprehensions and generator expressions |
| [`03_map_filter_sorted.py`](examples/03_map_filter_sorted.py) | `map`, `filter`, `sorted`, `reduce`, lazy iterators |
| [`04_iterators_and_generators.py`](examples/04_iterators_and_generators.py) | `iter`/`next`, `yield`, memory comparison, infinite generators |
| [`05_decorators.py`](examples/05_decorators.py) | `functools.wraps`, timing, parametrised, `@property`/`@staticmethod`/`@lru_cache` |

## Exercises

1. Add numbers with `*args`; print student details with `**kwargs`.
2. Square a number with a normal function, then with a `lambda`.
3. Print the even numbers from 1–10 using a list comprehension.
4. Sort a list of student dictionaries by a field with `sorted(key=...)`.

## Prerequisites

[Lesson 04 — Functions & Exceptions](../04-functions/)

## Next

[Interview prep](../../interview-prep/)
