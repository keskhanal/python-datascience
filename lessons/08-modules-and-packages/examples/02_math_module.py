"""The built-in `math` module."""

import math

print(math.pi, math.e)
print(math.sqrt(144))
print(math.pow(2, 10))          # returns a float, unlike 2 ** 10
print(math.floor(4.7), math.ceil(4.1), round(4.5))
print(math.factorial(5))
print(math.gcd(48, 18))
print(math.log(100, 10), math.log10(100))
print(math.inf, -math.inf, math.isnan(float("nan")))

# Degrees and radians
print(math.degrees(math.pi), math.radians(180))
print(round(math.sin(math.radians(30)), 4))

# math vs statistics
import statistics
marks = [85, 78, 92, 60, 78]
print(statistics.mean(marks), statistics.median(marks), statistics.mode(marks))
print(round(statistics.stdev(marks), 2))
