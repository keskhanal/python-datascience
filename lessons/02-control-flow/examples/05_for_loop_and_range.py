"""for loops and range()."""

# range(stop)
for i in range(5):
    print(i, end=" ")       # 0 1 2 3 4
print()

# range(start, stop)
for i in range(1, 6):
    print(i, end=" ")       # 1 2 3 4 5
print()

# range(start, stop, step)
for i in range(0, 21, 2):
    print(i, end=" ")       # even numbers up to 20
print()

# Counting backwards
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Looping over a string
for char in "Nepal":
    print(char, end="-")
print()

# enumerate() gives you the index too
for index, fruit in enumerate(["apple", "banana", "cherry"]):
    print(index, fruit)
