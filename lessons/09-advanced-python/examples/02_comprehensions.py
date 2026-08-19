"""List, dict and set comprehensions."""

# The long way
squares = []
for n in range(1, 11):
    squares.append(n ** 2)
print(squares)

# The comprehension way:  [expression for item in iterable]
print([n ** 2 for n in range(1, 11)])

# With a filter:  [expression for item in iterable if condition]
print([n for n in range(1, 21) if n % 2 == 0])

# With a conditional expression (note: the if/else comes FIRST)
print(["even" if n % 2 == 0 else "odd" for n in range(6)])

# Nested loops - read them top to bottom, like the for-loops they replace
print([(x, y) for x in [1, 2] for y in "ab"])

matrix = [[1, 2, 3], [4, 5, 6]]
print([n for row in matrix for n in row])          # flatten

# Dict comprehension
names = ["bibek", "asma", "hari"]
print({name: len(name) for name in names})

marks = {"bibek": 85, "asma": 92, "hari": 55}
print({n: m for n, m in marks.items() if m >= 60})

# Set comprehension
print({len(w) for w in ["hi", "there", "you", "are"]})

# Generator expression - same syntax with () - computed lazily, no list built
total = sum(n ** 2 for n in range(1, 1_000_001))
print(total)

# Keep them readable. If a comprehension needs a comment to understand,
# write it as a normal loop.
