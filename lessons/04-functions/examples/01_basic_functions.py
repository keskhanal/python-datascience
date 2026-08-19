"""Defining and calling functions."""

# No parameters, no return value
def greet():
    print("Hello!")

greet()

# One parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Asma")

# Returning a value - the caller decides what to do with it
def add(a, b):
    return a + b

result = add(10, 5)
print(result)

# A function without `return` gives back None
def no_return():
    print("I print but return nothing")

value = no_return()
print(value)          # None

# Returning multiple values (really a tuple)
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lowest, highest, average = stats([4, 8, 15, 16, 23, 42])
print(lowest, highest, round(average, 2))
