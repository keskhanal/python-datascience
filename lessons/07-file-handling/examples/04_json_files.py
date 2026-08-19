"""Working with JSON - the format most APIs and configs use."""

import json
import os

PATH = "students_demo.json"

students = [
    {"name": "Bibek", "age": 22, "addr": "ktm"},
    {"name": "Asma", "age": 20},
]

# Python object -> JSON file
with open(PATH, "w") as f:
    json.dump(students, f, indent=4)

# JSON file -> Python object
with open(PATH, "r") as f:
    loaded = json.load(f)

print(type(loaded), loaded)
print(loaded[0]["name"])

# Add a record and save it back
loaded.append({"name": "Hari", "age": 25, "addr": "pokhara"})
with open(PATH, "w") as f:
    json.dump(loaded, f, indent=4)

print(open(PATH).read())

# dumps / loads work on STRINGS instead of files (note the "s")
text = json.dumps({"ok": True, "count": 3})
print(type(text), text)
print(json.loads(text))

# JSON types map onto Python types:
#   object -> dict, array -> list, string -> str,
#   number -> int/float, true/false -> True/False, null -> None

os.remove(PATH)
