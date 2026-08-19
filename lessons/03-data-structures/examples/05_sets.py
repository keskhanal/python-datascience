"""Sets - unordered, no duplicates."""

nums = {1, 2, 3, 3, 2, 1}
print(nums)                       # {1, 2, 3} - duplicates dropped

# The classic use: de-duplicate a list
names = ["ram", "sita", "ram", "hari", "sita"]
print(list(set(names)))

s = {1, 2, 3}
s.add(4)
s.discard(1)                      # discard() will not error if missing
print(s)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b, "union")             # or a.union(b)
print(a & b, "intersection")      # or a.intersection(b)
print(a - b, "difference")        # in a but not in b
print(a ^ b, "symmetric difference")

# Membership tests on a set are much faster than on a list
print(3 in a)

# Sets are unordered - you cannot index them
try:
    print(a[0])
except TypeError as e:
    print("No indexing on sets:", e)
