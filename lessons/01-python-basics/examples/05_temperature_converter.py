"""Exercise solution: convert Fahrenheit to Celsius."""

fahrenheit = 97

celsius = (fahrenheit - 32) * (5 / 9)

print(f"{fahrenheit}F = {celsius:.2f}C")

# And back again
back = celsius * (9 / 5) + 32
print(f"{celsius:.2f}C = {back:.2f}F")
