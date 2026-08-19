"""Nested conditions: voting eligibility."""

age = 20
nationality = "Nepali"

if nationality == "Nepali":
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print(f"Not eligible yet - come back in {18 - age} year(s).")
else:
    print("Only Nepali citizens can vote here.")

# The same logic without nesting, using `and`
if nationality == "Nepali" and age >= 18:
    print("Eligible (flat version)")
