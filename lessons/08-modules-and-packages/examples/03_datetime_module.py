"""The `datetime` module: dates, times and differences."""

from datetime import datetime, date, timedelta

now = datetime.now()
print("now:", now)
print("today:", date.today())
print("year/month/day:", now.year, now.month, now.day)
print("weekday name:", now.strftime("%A"))

# strftime: datetime -> string
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d %B %Y, %I:%M %p"))

# strptime: string -> datetime
parsed = datetime.strptime("2024-08-15", "%Y-%m-%d")
print("parsed:", parsed, parsed.strftime("%A"))

# timedelta: date arithmetic
print("tomorrow:", date.today() + timedelta(days=1))
print("100 days ago:", date.today() - timedelta(days=100))

# Exercise: age calculator
def calculate_age(dob: date) -> int:
    today = date.today()
    years = today.year - dob.year
    # Subtract one if this year's birthday has not happened yet
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1
    return years

birthday = date(2002, 5, 17)
print(f"Born {birthday}, age is {calculate_age(birthday)}")
print("Days alive:", (date.today() - birthday).days)
