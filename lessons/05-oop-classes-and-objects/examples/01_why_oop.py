"""The same problem, written with functions and then with a class."""

# --- With functions and loose variables ---------------------------------
student1_name = "Bibek"
student1_marks = 85

def display(name, marks):
    print(f"{name}: {marks}")

display(student1_name, student1_marks)
# Add a second student and you are copy-pasting variables. The data and the
# functions that work on it are not connected.

# --- With a class -------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name            # data...
        self.marks = marks

    def display(self):              # ...and behaviour, bundled together
        print(f"{self.name}: {self.marks}")


s1 = Student("Bibek", 85)
s2 = Student("Asma", 78)
s1.display()
s2.display()

# One blueprint (the class), many objects (the instances).
print(type(s1), s1 is s2)
