"""input() always returns a string - convert before doing maths."""

# Simulating user input so the script runs without typing anything.
# In the notebook, replace these with: num1 = input("Enter first number: ")
num1 = "10"
num2 = "5"

print(num1 + num2)          # "105"  <- string concatenation, NOT addition!

# Convert to numbers first
a = int(num1)
b = int(num2)
print(a + b)                # 15

# Other conversions
print(float("3.14"))        # 3.14
print(str(42))              # "42"
print(int(3.99))            # 3      <- truncates, does not round
print(round(3.99))          # 4
print(bool(0), bool(""), bool("hi"))   # False False True

# Conversions that fail raise ValueError
try:
    int("ten")
except ValueError as e:
    print("Cannot convert:", e)
