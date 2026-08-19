"""The `random` module."""

import random

random.seed(42)      # same seed -> same "random" numbers, useful for teaching/tests

print(random.random())              # float in [0.0, 1.0)
print(random.randint(1, 6))         # integer, both ends INCLUDED
print(random.randrange(0, 10, 2))   # like range(), end excluded
print(round(random.uniform(1, 100), 2))

students = ["Bibek", "Asma", "Hari", "Gita", "Ram"]
print("random student:", random.choice(students))
print("random 3:", random.sample(students, 3))       # no repeats
print("with repeats:", random.choices(students, k=3))

shuffled = students.copy()
random.shuffle(shuffled)            # shuffles IN PLACE
print("shuffled:", shuffled)
print("original:", students)

# Weighted picks
print(random.choices(["pass", "fail"], weights=[80, 20], k=10))
