"""Dictionaries - key: value pairs."""

student = {
    "name": "Bibek",
    "age": 22,
    "marks": 85,
}

# Reading
print(student["name"])
print(student.get("addr"))                  # None instead of KeyError
print(student.get("addr", "not provided"))  # with a default

try:
    print(student["addr"])
except KeyError as e:
    print("KeyError:", e)

# Writing
student["addr"] = "Kathmandu"        # add a new key
student["age"] = 23                  # update an existing key
student.update({"marks": 90, "grade": "A"})
print(student)

# Deleting
del student["grade"]
removed = student.pop("addr")
print(student, "| removed:", removed)

# Looping
print(list(student.keys()))
print(list(student.values()))
for key, value in student.items():
    print(f"  {key}: {value}")

# Nested data - what real JSON/API responses look like
classroom = {
    "section": "A",
    "students": [
        {"name": "Asma", "marks": 78},
        {"name": "Hari", "marks": 92},
    ],
}
for s in classroom["students"]:
    print(f"{s['name']} scored {s['marks']}")
