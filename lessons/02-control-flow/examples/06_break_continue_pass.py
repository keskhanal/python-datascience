"""break, continue and pass."""

print("break - stop the loop immediately")
for n in range(1, 10):
    if n == 5:
        break
    print(n, end=" ")
print()

print("continue - skip this iteration, keep looping")
for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ")       # odd numbers only
print()

print("pass - do nothing (a placeholder so the block is not empty)")
for n in range(3):
    if n == 1:
        pass                # TODO: handle this case later
    print(n, end=" ")
print()
