"""Worked solutions for the lesson 04 exercises."""

def reverse_words(sentence: str) -> str:
    """Reverse the order of words in a sentence."""
    return " ".join(sentence.split()[::-1])


def largest(numbers: list) -> float:
    """Return the largest number - without using max()."""
    biggest = numbers[0]
    for n in numbers[1:]:
        if n > biggest:
            biggest = n
    return biggest


def grade_report(**students) -> dict:
    """Turn name=marks pairs into name -> grade."""
    def to_grade(marks):
        if marks >= 90:
            return "A"
        if marks >= 80:
            return "B"
        if marks >= 70:
            return "C"
        if marks >= 60:
            return "D"
        return "F"

    return {name: to_grade(marks) for name, marks in students.items()}


if __name__ == "__main__":
    print(reverse_words("python is really fun"))
    print(largest([4, 19, 3, 42, 7]), max([4, 19, 3, 42, 7]))
    print(grade_report(bibek=91, asma=74, hari=55))
