"""File modes: w, a, x, r+ - and what each one does."""

import os

PATH = "notes.txt"
if os.path.exists(PATH):
    os.remove(PATH)

# "w" - create or OVERWRITE. Everything already in the file is lost.
with open(PATH, "w") as f:
    f.write("first line\n")
    f.write("second line\n")

with open(PATH, "w") as f:            # note: this wipes the two lines above
    f.writelines(["alpha\n", "beta\n", "gamma\n"])

# "a" - append to the end, keep what is there
with open(PATH, "a") as f:
    f.write("delta\n")

with open(PATH) as f:                 # "r" is the default mode
    print(f.read())

# "x" - create, but fail if the file already exists
try:
    with open(PATH, "x") as f:
        f.write("nope")
except FileExistsError:
    print(f"{PATH} already exists - 'x' refused to overwrite it")

# Reading a file that is not there
try:
    open("does_not_exist.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

os.remove(PATH)
