"""A tour of standard-library modules worth knowing early."""

# --- collections: better containers -------------------------------------
from collections import Counter, defaultdict, namedtuple

words = "the quick brown fox jumps over the lazy dog the end".split()
print(Counter(words).most_common(3))

grouped = defaultdict(list)          # no KeyError on a missing key
for w in words:
    grouped[len(w)].append(w)
print(dict(grouped))

Point = namedtuple("Point", "x y")   # a lightweight, readable tuple
p = Point(3, 4)
print(p, p.x, p.y)

# --- itertools: looping tools -------------------------------------------
from itertools import combinations, product, groupby
print(list(combinations("ABC", 2)))
print(list(product([1, 2], "ab")))

# --- os and sys ----------------------------------------------------------
import os, sys
print("python:", sys.version.split()[0])
print("platform:", sys.platform)
print("HOME set:", "HOME" in os.environ)

# --- time --------------------------------------------------------------
import time
start = time.perf_counter()
sum(range(1_000_000))
print(f"took {time.perf_counter() - start:.4f}s")
