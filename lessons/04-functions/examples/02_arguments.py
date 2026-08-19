"""Positional, keyword and default arguments."""

def introduce(name, age, city="Kathmandu"):
    print(f"{name}, {age}, from {city}")

introduce("Bibek", 22)                       # positional
introduce("Asma", 20, "Pokhara")             # override the default
introduce(age=25, name="Hari")               # keyword args - order does not matter
introduce("Sita", city="Lalitpur", age=30)   # mix (positional must come first)

# Default values are evaluated ONCE, at definition time.
# This is the classic Python gotcha:
def add_item_buggy(item, basket=[]):         # BAD - the list is shared!
    basket.append(item)
    return basket

print(add_item_buggy("apple"))               # ['apple']
print(add_item_buggy("banana"))              # ['apple', 'banana']  <- surprise!

def add_item(item, basket=None):             # GOOD
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("apple"))                     # ['apple']
print(add_item("banana"))                    # ['banana']
