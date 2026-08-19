"""Arithmetic, comparison and logical operators."""

a, b = 17, 5

print("Arithmetic")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")    # true division -> float
print(f"{a} // {b} = {a // b}")   # floor division -> int
print(f"{a} % {b}  = {a % b}")    # remainder
print(f"{a} ** {b} = {a ** b}")   # exponent

print("\nComparison (result is always a bool)")
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

print("\nLogical")
age = 22
has_id = True
print(age >= 18 and has_id)   # both must be True
print(age >= 18 or has_id)    # at least one must be True
print(not has_id)             # flips it

print("\nAssignment shortcuts")
count = 10
count += 5   # same as count = count + 5
count *= 2
print(count)
