"""Tuples - ordered, UNchangeable, allow duplicates."""

point = (10, 20)
colors = ("red", "green", "blue")

print(point[0], colors[-1], len(colors))

# Tuples are immutable
try:
    point[0] = 99
except TypeError as e:
    print("Cannot modify a tuple:", e)

# Unpacking - very common in Python
x, y = point
print(f"x={x}, y={y}")

# Functions return tuples when they return "multiple values"
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 8, 1, 9])
print(low, high)

# A single-item tuple needs the trailing comma
not_a_tuple = ("hello")
real_tuple = ("hello",)
print(type(not_a_tuple), type(real_tuple))

# Use a tuple when the data must not change: coordinates, RGB values,
# database rows, dictionary keys.
