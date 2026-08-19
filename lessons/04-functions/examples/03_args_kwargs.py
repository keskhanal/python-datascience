"""*args and **kwargs - accepting any number of arguments."""

# *args collects extra POSITIONAL arguments into a tuple
def add_all(*args):
    print(type(args), args)
    return sum(args)

print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))
print(add_all())

# **kwargs collects extra KEYWORD arguments into a dictionary
def student_details(**kwargs):
    print(type(kwargs), kwargs)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

student_details(name="Bibek", age=22, grade="A")

# All four kinds together - the order is fixed:
# positional, *args, keyword-with-default, **kwargs
def report(title, *scores, passing=40, **extra):
    print(f"\n{title}: {scores}, passing={passing}, extra={extra}")
    print("  passed:", [s for s in scores if s >= passing])

report("Term 1", 35, 60, 88, passing=50, teacher="Ram", room="B2")

# Unpacking works in the other direction too
numbers = [1, 2, 3]
info = {"name": "Asma", "age": 20}
print(add_all(*numbers))     # unpack a list into positional args
student_details(**info)      # unpack a dict into keyword args
