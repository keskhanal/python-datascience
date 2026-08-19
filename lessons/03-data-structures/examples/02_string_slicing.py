"""Indexing and slicing: text[start:stop:step]."""

text = "Kathmandu"
#       0123456789
#      -9...     -1

print(text[0])        # K   - first character
print(text[-1])       # u   - last character
print(len(text))      # 9

print(text[0:4])      # Kath   - start is included, stop is NOT
print(text[:4])       # Kath   - start defaults to 0
print(text[4:])       # mandu  - stop defaults to len(text)
print(text[:])        # whole string

print(text[::2])      # Ktmnu  - every 2nd character
print(text[::-1])     # udnamhtaK  - reversed!

# Slicing works the same way on lists
nums = [10, 20, 30, 40, 50]
print(nums[1:4])      # [20, 30, 40]
print(nums[::-1])     # [50, 40, 30, 20, 10]
