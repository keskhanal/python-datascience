"""The different ways to import, and what each one gives you.

Run from the lesson folder so `maths` is importable:
    cd lessons/08-modules-and-packages
    python examples/01_import_styles.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1. Import the whole module - you keep the module name as a prefix
import maths
print(maths.sum_two_numbers(5, 10))

# 2. Import specific names - shorter to use, but can clash with your own names
from maths import multiply_two_numbers, divide_two_numbers
print(multiply_two_numbers(5, 10))

# 3. Import with an alias - the standard trick for long module names
import maths as m
print(m.sum_two_numbers(1, 2))

# 4. from module import *  -> AVOID. It hides where names came from.
# from maths import *

# A package: the folder's __init__.py decides what you get
from calculator import Calculator, greeting
print(greeting("Asma"))
print(Calculator().add(2, 3))

# Every module knows its own name. It is "__main__" only when run directly.
print("__name__ here is:", __name__)
print("maths.__name__ is:", maths.__name__)
