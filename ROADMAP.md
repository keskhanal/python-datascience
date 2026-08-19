# Roadmap — What's Left to Build

The repo currently takes a learner from "never written code" to comfortable, idiomatic
core Python (lessons 01–09). This file lists what is still missing to make it a complete
**basics → advanced → data science** path, in the order it should be taught.

Legend: ✅ done · 🟡 partly covered, needs its own lesson · ⬜ not started

---

## Part 1 — Core Python (lessons 01–09)

| Status | Topic | Where |
| ------ | ----- | ----- |
| ✅ | Variables, types, operators | [01](lessons/01-python-basics/) |
| ✅ | Conditionals and loops | [02](lessons/02-control-flow/) |
| ✅ | Strings, lists, tuples, sets, dicts | [03](lessons/03-data-structures/) |
| ✅ | Functions, `*args`/`**kwargs`, exceptions | [04](lessons/04-functions/) |
| ✅ | Classes, objects, inheritance, dunder methods | [05](lessons/05-oop-classes-and-objects/), [06](lessons/06-oop-inheritance/) |
| ✅ | Files, JSON, CSV, `os`/`pathlib` | [07](lessons/07-file-handling/) |
| ✅ | Modules, packages, standard library | [08](lessons/08-modules-and-packages/) |
| ✅ | Lambdas, comprehensions, generators, decorators | [09](lessons/09-advanced-python/) |

### Gaps to fill inside the existing lessons

- 🟡 **Exception handling** is introduced at the end of lesson 04 but never expanded —
  custom exception classes, exception chaining, and `logging` instead of `print()`
  deserve their own lesson (see 10 below).
- 🟡 **`match`/`case`** in lesson 02 only matches literals. Add structural patterns
  (matching dicts and lists) once dictionaries are taught in lesson 03.
- 🟡 **No exercise solutions for lessons 05, 06 and 08.** Lessons 01–04, 07 and 09 have
  `examples/*_exercises_solved.py`; the OOP and modules lessons still need theirs.
- 🟡 **No tests anywhere.** Once lesson 13 (testing) exists, add a `tests/` folder per
  lesson so learners can check their own exercise solutions with `pytest`.
- 🟡 **Notebook outputs are committed.** Consider clearing them before commit
  (`jupyter nbconvert --clear-output --inplace`) so diffs stay readable.

---

## Part 2 — Intermediate Python (⬜ not started)

| # | Lesson | Topics |
| - | ------ | ------ |
| 10 | **Errors, Debugging & Logging** | Exception hierarchy, custom exception classes, `raise ... from`, `assert`, the `logging` module, `breakpoint()`/pdb, reading a traceback |
| 11 | **Advanced OOP** | `@dataclass`, abstract base classes (`abc`), composition vs. inheritance, mixins, `__slots__`, `Enum`, when *not* to use a class |
| 12 | **Type Hints & Clean Code** | `list[int]`, `dict[str, float]`, `Optional`, `Union`/`\|`, `TypedDict`, `Protocol`, running `mypy`, PEP 8, `ruff`/`black` formatting |
| 13 | **Testing with pytest** | `assert`, test discovery, fixtures, `parametrize`, mocking, coverage, test-driven development on a small exercise |
| 14 | **Regular Expressions** | `re.search`/`findall`/`sub`, groups, character classes, validating emails and phone numbers, cleaning messy text |
| 15 | **Functional Python & itertools** | `functools` (`partial`, `reduce`, `lru_cache`), `itertools` recipes, closures, first-class functions, immutability |
| 16 | **Concurrency** | `threading` vs. `multiprocessing` vs. `asyncio`, the GIL, `concurrent.futures`, `async`/`await`, when each one actually helps |
| 17 | **Working with APIs** | HTTP basics, `requests`, headers and auth, pagination, rate limits, parsing JSON responses, error handling and retries |
| 18 | **Databases & SQL** | `sqlite3` from Python, SELECT/INSERT/UPDATE/DELETE, joins, parameterised queries (SQL injection), a first look at SQLAlchemy |

---

## Part 3 — Tooling & Environment (⬜ not started)

| # | Lesson | Topics |
| - | ------ | ------ |
| 19 | **Environments & Dependencies** | `venv`, `pip`, `requirements.txt` vs. `pyproject.toml`, `uv`/`poetry`, pinning versions, why a global install goes wrong |
| 20 | **Git & GitHub for Learners** | init/add/commit/push, branches, pull requests, `.gitignore`, resolving conflicts, committing notebooks safely |
| 21 | **Project Structure & Packaging** | `src/` layout, `pyproject.toml`, entry points, publishing to PyPI, writing a README that someone can follow |
| 22 | **The Command Line & Automation** | `argparse`, environment variables and `.env`, cron/scheduled scripts, `subprocess` |

---

## Part 4 — Data Science (⬜ not started — the course name promises this)

| # | Lesson | Topics |
| - | ------ | ------ |
| 23 | **NumPy** | `ndarray` vs. list, dtypes, shape/reshape, indexing and boolean masks, broadcasting, vectorised maths, `axis=` |
| 24 | **pandas — Foundations** | `Series` and `DataFrame`, reading CSV/JSON/Excel, `head`/`info`/`describe`, selection with `loc`/`iloc`, filtering |
| 25 | **pandas — Data Wrangling** | Missing values, dtype conversion, `groupby`/`agg`, `merge`/`join`, `pivot_table`, `apply`, dates and time series |
| 26 | **Data Cleaning in Practice** | A genuinely messy real dataset: duplicates, inconsistent categories, outliers, text normalisation, validation |
| 27 | **Visualisation** | matplotlib fundamentals (figure/axes), line/bar/scatter/histogram, seaborn, choosing the right chart, labelling for a reader |
| 28 | **Statistics for Data Science** | Mean/median/mode, spread, distributions, correlation vs. causation, sampling, hypothesis testing, p-values |
| 29 | **Exploratory Data Analysis** | A full EDA on one dataset end to end — question → clean → explore → visualise → conclusion |
| 30 | **Intro to Machine Learning** | scikit-learn API, train/test split, linear and logistic regression, decision trees, over/underfitting, evaluation metrics |
| 31 | **ML in Practice** | Feature engineering, pipelines, cross-validation, hyperparameter tuning, saving and loading a model |

---

## Part 5 — Projects (1 of ~6 done)

| Status | Project | Skills it proves |
| ------ | ------- | ---------------- |
| ✅ | [Library Management System](projects/library-management-system/) | OOP, composition, validation |
| ⬜ | **Student Result Management (CLI)** | Files + JSON persistence, functions, menus (after lesson 07) |
| ⬜ | **Expense Tracker** | CSV, dates, `argparse`, aggregation (after lesson 22) |
| ⬜ | **Weather / News API Client** | `requests`, JSON, error handling, caching (after lesson 17) |
| ⬜ | **Sales Data Analysis** | pandas + matplotlib on a real CSV (after lesson 27) |
| ⬜ | **Capstone: End-to-End ML** | Data cleaning → EDA → model → written report (after lesson 31) |

---

## Also Worth Adding

- ⬜ **`CONTRIBUTING.md`** — how students should submit exercise solutions (branch + PR).
- ⬜ **`CHEATSHEET.md`** — one printable page per part: syntax, methods, common errors.
- ⬜ **A glossary** — plain-English definitions of iterable, mutable, instance, scope,
  argument vs. parameter, and the other words that quietly block beginners.
- ⬜ **Common-errors reference** — `IndentationError`, `NameError`, `TypeError`,
  `KeyError`, `IndexError`, `ModuleNotFoundError`: what each one really means.
- ⬜ **Solutions branch or folder** so exercise answers are available but not spoilers.
- ⬜ **CI** — a GitHub Action that runs every `examples/*.py` and the future `pytest`
  suite, so a broken example is caught before a student hits it.

---

## Suggested Order for Filling This In

1. Lesson 10 (errors/logging) and 11 (advanced OOP) — they finish the core-Python story.
2. Lesson 19 (environments) and 20 (git) — students need these to submit work at all.
3. Lessons 23–25 (NumPy and pandas) — the actual data science the course is named for.
4. Lesson 13 (testing) plus a `tests/` folder per lesson, so exercises become self-checking.
5. Everything else, in the numbered order above.
