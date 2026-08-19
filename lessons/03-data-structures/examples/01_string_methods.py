"""The string methods you will use every day."""

text = "  Hello, Python World!  "

print(repr(text.strip()))          # remove surrounding whitespace
print(text.strip().upper())
print(text.strip().lower())
print(text.strip().title())
print(text.replace("Python", "Data Science").strip())

sentence = "python is fun and python is powerful"
print(sentence.count("python"))    # 2
print(sentence.find("fun"))        # index of first match, -1 if not found
print(sentence.startswith("python"), sentence.endswith("!"))

# split() -> list, join() -> string
words = sentence.split()           # splits on whitespace by default
print(words)
print("-".join(words))

csv_row = "bibek,22,ktm"
print(csv_row.split(","))

# Strings are immutable: methods return a NEW string
original = "hello"
original.upper()
print(original)                    # still "hello"
original = original.upper()        # you must reassign
print(original)
