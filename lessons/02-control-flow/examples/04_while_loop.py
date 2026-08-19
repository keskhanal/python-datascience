"""while loops - repeat until a condition becomes False."""

# Count 1 to 5
i = 1
while i <= 5:
    print("python", i)
    i += 1          # forget this line and the loop runs forever

# while with a sentinel value (menu pattern)
options = ["1", "2", "3"]   # pretend these came from input()
for choice in options:
    if choice == "3":
        print("Exiting...")
        break
    print(f"You picked option {choice}")

# while ... else: the else runs only if the loop was NOT broken out of
n = 3
while n > 0:
    n -= 1
else:
    print("Loop finished normally")
