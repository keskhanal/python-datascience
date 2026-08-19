"""Several children from one parent, and a chain of inheritance."""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns {self.salary}"


# --- Hierarchical: two siblings from the same parent ---
class Developer(Employee):
    def describe(self):
        return super().describe() + " writing code"


class Manager(Employee):
    def describe(self):
        return super().describe() + " managing a team"


# --- Multilevel: a child of a child ---
class TeamLead(Developer):
    def describe(self):
        return super().describe() + " and leading the team"


for e in [Employee("Ram", 40_000), Developer("Sita", 60_000), Manager("Hari", 80_000), TeamLead("Gita", 90_000)]:
    print(e.describe())
