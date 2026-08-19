"""__init__, self, instance attributes, class attributes and methods."""

class Student:
    school = "Vrit Academy"      # CLASS attribute - shared by every instance
    count = 0

    def __init__(self, name, age, marks):
        # INSTANCE attributes - unique to each object
        self.name = name
        self.age = age
        self.marks = marks
        Student.count += 1       # bump the shared counter

    def display_info(self):
        """An instance method: it receives the object as `self`."""
        print(f"{self.name} ({self.age}) - {self.marks} marks at {self.school}")

    def is_pass(self, passing=40):
        return self.marks >= passing

    def __str__(self):
        """What print(object) shows."""
        return f"Student({self.name}, {self.marks})"


s1 = Student("Bibek", 22, 85)
s2 = Student("Asma", 20, 35)

s1.display_info()
s2.display_info()
print(s1.is_pass(), s2.is_pass())
print("Students created:", Student.count)
print(s1)                        # uses __str__

# You never pass `self` yourself - Python does it:
Student.display_info(s1)         # exactly what s1.display_info() becomes
