# Lesson 03 — Data Structures

**Day 3** · Notebook: [`data_structures.ipynb`](data_structures.ipynb)

Python's four built-in collections, plus string methods. Opens with a revision of Lesson 02.

## Topics

- **Strings** — `len()`, slicing, `upper()`, `strip()`, `replace()`, `split()`, `join()`,
  `find()`, `count()`
- **Lists** — indexing, `append()`, `pop()`, mutability
- **Tuples** — immutability and when to prefer them
- **Sets** — uniqueness, `union()` and other set operations
- **Dictionaries** — key/value access, `get()` for safe access, `update()`, `del`,
  `keys()`, `values()`, looping over items

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_string_methods.py`](examples/01_string_methods.py) | `strip`, `split`, `join`, `replace`, immutability |
| [`02_string_slicing.py`](examples/02_string_slicing.py) | `[start:stop:step]`, negative indexes, reversing |
| [`03_lists.py`](examples/03_lists.py) | Add/remove/sort, and the copy-vs-reference trap |
| [`04_tuples.py`](examples/04_tuples.py) | Immutability, unpacking, single-item tuples |
| [`05_sets.py`](examples/05_sets.py) | De-duplication and set algebra |
| [`06_dictionaries.py`](examples/06_dictionaries.py) | `get()` vs `[]`, looping, nested data |
| [`07_exercises_solved.py`](examples/07_exercises_solved.py) | Palindrome, prime, char-frequency solutions |

## Exercises

1. Print even numbers up to 20.
2. Sum the first N numbers.
3. "Guess the secret number" game.
4. ATM simulator.
5. Check whether a number is prime.
6. Reverse the words in a sentence.
7. Check whether a word is a palindrome (case-insensitive), with and without a loop.

## Prerequisites

[Lesson 02 — Control Flow](../02-control-flow/)

## Next

[Lesson 04 — Functions & Exceptions](../04-functions/)
