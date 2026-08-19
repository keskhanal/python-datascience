"""Variables and the four basic data types."""

# int - whole numbers
age = 25
# float - decimal numbers
height = 5.9
# str - text
name = "Bibek"
# bool - True / False
is_student = True

print(name, age, height, is_student)

# type() tells you what a value is
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(name))        # <class 'str'>
print(type(is_student))  # <class 'bool'>

# Variables can be reassigned to a different type (Python is dynamically typed)
age = "twenty five"
print(type(age))         # <class 'str'>

# Naming conventions
first_name = "Asma"      # snake_case  -> good
PI = 3.14159             # UPPER_CASE  -> constant by convention
print(first_name, PI)
# 1name = "x"            # SyntaxError: cannot start with a digit
# first-name = "x"       # SyntaxError: hyphens are not allowed
