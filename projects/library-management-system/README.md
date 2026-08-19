# Project — Library Management System

**Notebook:** [`library_management_system.ipynb`](library_management_system.ipynb)

An end-to-end OOP project that ties together everything from lessons 01–06: multiple
classes that collaborate, with validation and state that changes over time.

## What You Build

| Class | Responsibility |
| ----- | -------------- |
| `Book` | Title, author, ISBN, and availability |
| `Member` | A borrower, and the books they currently hold |
| `Library` | Owns the catalogue; handles adding books, registering members, borrowing and returning |

The notebook finishes with a testing section that exercises the classes together.

## Concepts Practised

- Classes, `__init__`, instance attributes and methods (Lesson 05)
- Composition — objects holding other objects
- Validation with `re` (regular expressions)
- Lists and dictionaries as in-memory storage (Lesson 03)

## Prerequisites

[Lesson 06 — OOP: Inheritance](../../lessons/06-oop-inheritance/)

## Extension Ideas

- Persist the catalogue to `library.json` using what you learned in
  [Lesson 07](../../lessons/07-file-handling/).
- Add a due date and an overdue-fine calculation.
- Add a `Librarian` subclass of `Member` with extra permissions.
