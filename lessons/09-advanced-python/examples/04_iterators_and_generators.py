"""Iterators vs generators: lazy evaluation."""

# --- Iterator: what a for loop does under the hood -----------------------
nums = [1, 2, 3]
it = iter(nums)
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("StopIteration - the for loop catches this for you")

# Writing your own iterator class is verbose:
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print(list(CountDown(5)))


# --- Generator: the same thing with `yield` ------------------------------
def countdown(start):
    while start > 0:
        yield start          # pause here, hand back a value, resume on next()
        start -= 1

print(list(countdown(5)))

# Why it matters: generators do not build the whole result in memory
def first_n_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

gen = first_n_squares(1_000_000)   # instant - nothing computed yet
print(next(gen), next(gen), next(gen))

import sys
print("list  bytes:", sys.getsizeof([n for n in range(100_000)]))
print("gen   bytes:", sys.getsizeof(n for n in range(100_000)))

# An infinite generator is fine, because it is lazy
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fibonacci(), 10)))

# Reading a huge file line by line is the classic real-world generator
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
