"""CSV files - the format you will meet constantly in data science."""

import csv
import os

PATH = "marks.csv"

rows = [
    ["name", "subject", "marks"],
    ["Bibek", "Python", 85],
    ["Asma", "Python", 78],
    ["Hari", "Python", 92],
]

# Writing. newline="" avoids blank rows on Windows.
with open(PATH, "w", newline="") as f:
    csv.writer(f).writerows(rows)

# Reading as lists
with open(PATH, newline="") as f:
    for row in csv.reader(f):
        print(row)

# Reading as dictionaries - usually what you want
print()
with open(PATH, newline="") as f:
    total = 0
    for row in csv.DictReader(f):
        print(f"{row['name']:<8} {row['marks']}")
        total += int(row["marks"])
    print("average:", total / 3)

# Writing dictionaries
with open(PATH, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerow({"name": "Gita", "marks": 88})

print("\n" + open(PATH).read())
os.remove(PATH)
