# Python for Data Science — Course Materials

A hands-on, day-by-day Python course taught through Jupyter notebooks. Each lesson is a
self-contained folder with its own notebook(s), sample data, and a README listing the
topics and exercises covered.

## Course Structure

```
datascience-course/
├── lessons/                 # numbered lessons, in teaching order
│   └── 01-python-basics/
│       ├── README.md        # topics, examples index, exercises
│       ├── python_basics.ipynb
│       └── examples/        # small runnable .py scripts, one per concept
├── projects/                # larger end-of-topic projects
├── interview-prep/          # interview questions and classic problems
├── ROADMAP.md               # what is still missing, and in what order
└── requirements.txt
```

Every lesson follows the same shape: a **README** (what you will learn), a **notebook**
(taught live, with exercises), and an **`examples/`** folder of short scripts you can run
and edit on your own. Run any example with `python examples/<file>.py` from its lesson folder.

## Syllabus

| Day | Lesson | Topics |
| --- | ------ | ------ |
| 1 | [01 — Python Basics](lessons/01-python-basics/) | Comments, `input()`, variables, data types, type conversion, operators |
| 2 | [02 — Control Flow](lessons/02-control-flow/) | `if`/`elif`/`else`, nested conditions, `match`, `while`, `for`, `break`/`continue`/`pass` |
| 3 | [03 — Data Structures](lessons/03-data-structures/) | Strings & slicing, lists, tuples, sets, dictionaries |
| 4 | [04 — Functions & Exceptions](lessons/04-functions/) | Parameters, return values, scope, `*args`/`**kwargs`, type hints, docstrings, `try`/`except` |
| 5 | [05 — OOP: Classes & Objects](lessons/05-oop-classes-and-objects/) | Classes, objects, `__init__`, attributes, methods |
| 6 | [06 — OOP: Inheritance](lessons/06-oop-inheritance/) | Single & hierarchical inheritance, method overriding, `super()`, dunder methods |
| 7 | [07 — File Handling](lessons/07-file-handling/) | File modes, read/write/append, `with`, `os` module, JSON files |
| 8 | [08 — Modules & Packages](lessons/08-modules-and-packages/) | `import`, built-in modules (`math`, `datetime`, `random`), user-defined modules & packages |
| 9 | [09 — Advanced Python](lessons/09-advanced-python/) | Lambdas, comprehensions, `map`/`filter`/`sorted`, iterators, generators, decorators |

### Projects

- [Library Management System](projects/library-management-system/) — applies OOP (lesson 5–6) to a
  multi-class system with books, members, and borrowing rules.

### Interview Prep

- [Python interview questions](interview-prep/) — shallow vs. deep copy, `is` vs. `==`, and
  common coding problems.

## What This Course Does Not Cover *Yet*

Lessons 01–09 cover core Python thoroughly. The intermediate topics (testing, type hints,
concurrency, APIs, databases) and the data science stack (NumPy, pandas, matplotlib,
scikit-learn) are still to be written — see **[ROADMAP.md](ROADMAP.md)** for the full plan,
the gaps in the current lessons, and the order in which to fill them.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd datascience-course
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Jupyter and open a lesson:

   ```bash
   jupyter notebook
   ```

   Or open the folder in VS Code with the Jupyter extension and pick the `.venv` kernel.

## How to Work Through a Lesson

- Read the lesson `README.md` first — it lists the topics and the exercises in the notebook.
- Run the notebook cells top to bottom; each lesson opens with a short revision of the previous one.
- Notebooks use **relative paths**, so run them with the lesson folder as the working directory
  (Jupyter and VS Code do this automatically when you open the notebook from its folder).
- Run and modify the scripts in `examples/` — breaking them on purpose is the fastest way
  to learn what each error message means.
- Attempt the exercises at the end of each notebook before moving on.
