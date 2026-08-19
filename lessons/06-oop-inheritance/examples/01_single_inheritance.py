"""Single inheritance: a child class reuses a parent."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old.")


class Student(Person):               # Student IS-A Person
    def __init__(self, name, age, college):
        super().__init__(name, age)  # let Person set up name and age
        self.college = college       # then add what is new

    def study(self):
        print(f"{self.name} is studying at {self.college}.")


s = Student("Asma", 20, "Vrit College")
s.introduce()     # inherited from Person
s.study()         # defined on Student

print(isinstance(s, Student), isinstance(s, Person))
print(Student.__mro__)   # the order Python searches for methods
