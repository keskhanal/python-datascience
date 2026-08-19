"""Every way to read a text file."""

PATH = "sample.txt"

# Set up a file to read
with open(PATH, "w") as f:
    f.write("Harry\nRon\nHermione\nBhagawati\n")

# read() - the whole file as one string
with open(PATH, "r") as f:
    print(repr(f.read()))

# read(n) - only n characters
with open(PATH, "r") as f:
    print(repr(f.read(5)))

# readline() - one line at a time (keeps the trailing \n)
with open(PATH, "r") as f:
    print(repr(f.readline()))
    print(repr(f.readline()))

# readlines() - a list of lines
with open(PATH, "r") as f:
    print(f.readlines())

# Looping over the file object - the memory-friendly way for big files
with open(PATH, "r") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())

import os
os.remove(PATH)
