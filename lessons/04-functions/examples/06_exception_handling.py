"""try / except / else / finally."""

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"  Wrong type: {e}")
        return None
    else:
        print("  No error occurred")     # runs only if try succeeded
        return result
    finally:
        print("  finally always runs (cleanup goes here)")

print("10 / 2 ->", safe_divide(10, 2))
print("10 / 0 ->", safe_divide(10, 0))
print("10 / 'a' ->", safe_divide(10, "a"))

# Converting user input safely
for raw in ["42", "abc"]:
    try:
        print(int(raw) * 2)
    except ValueError:
        print(f"'{raw}' is not a number")

# Raising your own errors
def set_age(age: int):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Caught:", e)

# Bare `except:` hides real bugs. Always catch the specific exception you expect.
