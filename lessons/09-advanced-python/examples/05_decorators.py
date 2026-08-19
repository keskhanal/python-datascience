"""Decorators: wrapping a function to add behaviour around it."""

import functools
import time

# A function is just an object - you can pass it around and nest it.
def shout(func):
    @functools.wraps(func)              # keeps the original name and docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper() + "!!!"
    return wrapper


@shout                                  # same as: greet = shout(greet)
def greet(name):
    """Say hello."""
    return f"hello {name}"

print(greet("asma"))
print(greet.__name__, "|", greet.__doc__)   # thanks to functools.wraps


# --- A timing decorator - the classic real use case ---------------------
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)


# --- A decorator that takes arguments (one more layer) ------------------
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def ping():
    print("ping")

ping()


# --- Built-in decorators you will meet ----------------------------------
class Circle:
    def __init__(self, r):
        self.r = r

    @property                       # call it like an attribute
    def area(self):
        return 3.14159 * self.r ** 2

    @staticmethod                   # no self - just a function living in the class
    def unit():
        return "cm"

    @classmethod                    # receives the class, not the instance
    def from_diameter(cls, d):
        return cls(d / 2)


c = Circle.from_diameter(10)
print(round(c.area, 2), Circle.unit())


@functools.lru_cache(maxsize=None)  # caches results - turns O(2^n) into O(n)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))
