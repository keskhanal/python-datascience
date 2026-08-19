"""Lists - ordered, changeable, allow duplicates."""

fruits = ["apple", "banana", "cherry"]

# Adding
fruits.append("mango")            # add to the end
fruits.insert(1, "orange")        # add at a position
fruits.extend(["kiwi", "guava"])  # add many
print(fruits)

# Removing
fruits.remove("banana")           # by value (first match)
last = fruits.pop()               # removes and returns the last item
second = fruits.pop(1)            # by index
del fruits[0]                     # by index, no return value
print(fruits, "| removed:", last, second)

# Reading
print(fruits[0], fruits[-1], len(fruits))
print("kiwi" in fruits)           # membership test

# Ordering
nums = [5, 2, 9, 1, 7]
nums.sort()                       # sorts in place
print(nums)
nums.sort(reverse=True)
print(nums)
print(sorted(nums))               # returns a NEW sorted list
nums.reverse()
print(nums)

# Careful: assignment does not copy
a = [1, 2, 3]
b = a                             # b points at the SAME list
b.append(4)
print(a)                          # [1, 2, 3, 4]
c = a.copy()                      # a real copy
c.append(5)
print(a, c)
