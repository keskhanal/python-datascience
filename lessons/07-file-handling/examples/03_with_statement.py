"""Why `with` is better than open()/close()."""

PATH = "demo.txt"

# The manual way - you must remember to close, and an exception skips close()
f = open(PATH, "w")
f.write("hello\n")
f.close()
print("closed?", f.closed)

# The `with` way - the file is closed automatically, even if an error is raised
try:
    with open(PATH, "r") as f:
        print(f.read().strip())
        raise ValueError("something went wrong mid-read")
except ValueError as e:
    print("Caught:", e)
print("closed?", f.closed)            # True - `with` cleaned up for us

# Reading one file and writing another at the same time
with open(PATH) as src, open("copy.txt", "w") as dst:
    dst.write(src.read().upper())

with open("copy.txt") as f:
    print(f.read().strip())

import os
os.remove(PATH)
os.remove("copy.txt")
