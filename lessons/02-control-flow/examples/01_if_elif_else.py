"""Branching with if / elif / else."""

marks = 76

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks} -> Grade: {grade}")

# Order matters. If you check `marks >= 60` first, everyone above 60 gets a D.

# A one-line conditional (ternary) for simple cases
status = "Pass" if marks >= 40 else "Fail"
print(status)
