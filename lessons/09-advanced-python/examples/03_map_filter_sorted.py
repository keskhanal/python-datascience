"""map(), filter(), sorted() and reduce()."""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(function, iterable) - apply a function to every item
print(list(map(lambda n: n ** 2, nums)))
print([n ** 2 for n in nums])                 # the comprehension equivalent

# map over several iterables at once
a, b = [1, 2, 3], [10, 20, 30]
print(list(map(lambda x, y: x * y, a, b)))

# A very common use: convert a list of strings to numbers
print(list(map(int, ["1", "2", "3"])))

# filter(function, iterable) - keep the items where the function is True
print(list(filter(lambda n: n % 2 == 0, nums)))
print([n for n in nums if n % 2 == 0])

# filter with None drops every falsy value
print(list(filter(None, [0, 1, "", "hi", None, [], [1]])))

# sorted(iterable, key=..., reverse=...)
words = ["banana", "Fig", "apple", "cherry"]
print(sorted(words))                          # capitals sort first
print(sorted(words, key=str.lower))           # case-insensitive
print(sorted(words, key=len, reverse=True))

# reduce(function, iterable) - fold the whole iterable into one value
print(reduce(lambda acc, n: acc + n, nums))       # same as sum(nums)
print(reduce(lambda acc, n: acc * n, [1,2,3,4,5]))  # factorial of 5

# map/filter return lazy iterators - they are consumed once
m = map(str.upper, ["a", "b"])
print(list(m), list(m))                       # second call is empty!
