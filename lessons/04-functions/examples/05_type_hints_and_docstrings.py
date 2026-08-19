"""Type hints and docstrings - how to document a function."""

def calculate_grade(marks: float, total: float = 100.0) -> str:
    """Convert marks into a letter grade.

    Args:
        marks: Marks the student scored.
        total: Maximum possible marks. Defaults to 100.

    Returns:
        A letter grade from "A" to "F".

    Raises:
        ValueError: If total is zero or negative.
    """
    if total <= 0:
        raise ValueError("total must be greater than zero")

    percent = (marks / total) * 100
    if percent >= 90:
        return "A"
    if percent >= 80:
        return "B"
    if percent >= 70:
        return "C"
    if percent >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    print(calculate_grade(85))
    print(calculate_grade(38, total=50))
    print(calculate_grade.__doc__)      # the docstring is readable at runtime
    help(calculate_grade)               # ...and by help()

    # Type hints are NOT enforced at runtime - they are for readers and tools
    # like mypy, pyright and your editor's autocomplete.
