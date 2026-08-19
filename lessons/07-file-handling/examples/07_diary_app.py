"""Exercise solution: the personal diary, as a menu-driven program.

Run it with:  python 07_diary_app.py
The input() calls are real, so this one is interactive.
"""

from datetime import datetime

DIARY = "diary.txt"


def write_entry():
    entry = input("What happened today? ")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DIARY, "a") as f:
        f.write(f"[{stamp}] {entry}\n")
    print("Saved.\n")


def read_diary():
    try:
        with open(DIARY) as f:
            content = f.read()
    except FileNotFoundError:
        print("No entries yet.\n")
        return
    print("\n--- Your diary ---")
    print(content if content else "(empty)")


def main():
    while True:
        print("1. Write entry")
        print("2. Read diary")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_diary()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
