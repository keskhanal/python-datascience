# Lesson 06 — OOP: Inheritance

**Day 6** · Notebook: [`inheritance_and_overriding.ipynb`](inheritance_and_overriding.ipynb)

Reusing and extending classes. Opens with a revision of Lesson 05.

## Topics

- Single inheritance
- Hierarchical inheritance
- Method overriding
- `super()`
- Magic (dunder) methods — `__str__`, `__len__`, and friends

## Examples

| Script | Shows |
| ------ | ----- |
| [`01_single_inheritance.py`](examples/01_single_inheritance.py) | `super()`, `isinstance()`, the MRO |
| [`02_hierarchical_and_multilevel.py`](examples/02_hierarchical_and_multilevel.py) | Sibling subclasses and inheritance chains |
| [`03_overriding_and_polymorphism.py`](examples/03_overriding_and_polymorphism.py) | Overriding, polymorphism, duck typing |
| [`04_dunder_methods.py`](examples/04_dunder_methods.py) | `__str__`, `__repr__`, `__add__`, `__eq__`, `__len__`, `__getitem__` |
| [`05_encapsulation_and_properties.py`](examples/05_encapsulation_and_properties.py) | `_protected`, `__private`, `@property` and setters |

## Exercises

1. Banking system — `Account` with deposit/withdraw, extended by account subtypes.
2. `Person` → `RetiredPerson` hierarchy with an overridden method.

## Prerequisites

[Lesson 05 — OOP: Classes & Objects](../05-oop-classes-and-objects/)

## Next

[Lesson 07 — File Handling](../07-file-handling/) ·
Project: [Library Management System](../../projects/library-management-system/)
