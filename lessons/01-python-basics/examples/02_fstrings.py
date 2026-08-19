"""Formatting output with f-strings."""

name = "Hermione"
age = 20
marks = 87.4567

# Old way
print("My name is " + name + " and I am " + str(age) + " years old.")

# f-string way - readable, and no str() needed
print(f"My name is {name} and I am {age} years old.")

# Expressions work inside the braces
print(f"Next year I will be {age + 1}.")

# Round a float to 2 decimal places
print(f"Marks: {marks:.2f}")

# Pad and align (useful for tables)
print(f"|{'Name':<10}|{'Marks':>8}|")
print(f"|{name:<10}|{marks:>8.2f}|")
