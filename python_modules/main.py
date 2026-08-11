# from student import student
from student.student import Student

if __name__ == "__main__":
    student1 = Student("Alice", 20, 85)
    student1.display_info()
    print(f"Grade: {student1.calculate_grade()}")
    print(f"Has Passed: {student1.has_passed()}")

    student2 = Student("Bob", 22, 55)
    student2.display_info()
    print(f"Grade: {student2.calculate_grade()}")
    print(f"Has Passed: {student2.has_passed()}")