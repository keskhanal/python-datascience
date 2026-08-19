"""Lambda: a small, unnamed function written in one line."""

# A normal function...
def square(n):
    return n ** 2

# ...and the same thing as a lambda
square_lambda = lambda n: n ** 2
print(square(5), square_lambda(5))

add = lambda a, b: a + b
print(add(3, 4))

# Lambdas shine as throwaway arguments to other functions
students = [
    {"name": "Bibek", "marks": 85},
    {"name": "Asma", "marks": 92},
    {"name": "Hari", "marks": 78},
]
print(sorted(students, key=lambda s: s["marks"], reverse=True))
print(max(students, key=lambda s: s["marks"])["name"])

pairs = [(2, "b"), (1, "c"), (3, "a")]
print(sorted(pairs, key=lambda p: p[1]))     # sort by the letter

# A lambda can only hold ONE expression - no statements, no loops.
# If it needs a name or more than one line, write a def instead.
