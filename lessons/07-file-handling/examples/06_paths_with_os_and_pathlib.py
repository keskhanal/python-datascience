"""Locating files: the os module and the modern pathlib."""

import os
from pathlib import Path

# --- os ------------------------------------------------------------------
print("cwd:", os.getcwd())
print("this folder:", os.listdir("."))

path = "student.txt"
print("exists:", os.path.exists(path))
if os.path.exists(path):
    print("size:", os.path.getsize(path), "bytes")

print("joined:", os.path.join("data", "raw", "students.csv"))
print("split:", os.path.splitext("report.final.csv"))

os.makedirs("output/reports", exist_ok=True)   # creates parents, no error if present
print("created output/reports")

# --- pathlib (preferred in modern Python) --------------------------------
here = Path(__file__).parent
lesson_folder = here.parent
print("\nlesson folder:", lesson_folder.name)
print("notebooks here:", [p.name for p in lesson_folder.glob("*.ipynb")])

target = lesson_folder / "student.txt"          # the / operator joins paths
print("target:", target.name, "| exists:", target.exists())
if target.exists():
    print("first line:", target.read_text().splitlines()[0])

# Tidy up
os.rmdir("output/reports")
os.rmdir("output")
