"""create a Student class, with attributes name, age, and marks. Implement a method to display the student's information 
method to calculate grade based on marks,
and another method to determine if the student has passed based on a passing grade threshold.
"""
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

    def has_passed(self):
        passing_grade = {"A", "B", "C", "D"}
        grade = self.calculate_grade()
        if grade in passing_grade:
            return True
        else:
            return False
        # return grade in passing_grade

    
# Example usage
# if __name__ == "__main__":
#     # student1 = Student("Alice", 20, 85)
#     # student1.display_info()
#     # print(f"Grade: {student1.calculate_grade()}")
#     # print(f"Has Passed: {student1.has_passed()}")

#     # student2 = Student("Bob", 22, 55)
#     # student2.display_info()
#     # print(f"Grade: {student2.calculate_grade()}")
#     # print(f"Has Passed: {student2.has_passed()}")
#     print("Student module loaded successfully.")