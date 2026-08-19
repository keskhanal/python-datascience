"""match / case - Python 3.10+ structural pattern matching."""

def describe_day(day: str) -> str:
    match day.lower():
        case "saturday":
            return "Weekend - holiday!"
        case "sunday" | "monday" | "tuesday" | "wednesday" | "thursday":
            return "Working day"
        case "friday":
            return "Half day"
        case _:                      # _ is the default / catch-all
            return "Not a real day"

for d in ["Saturday", "Monday", "Friday", "Funday"]:
    print(f"{d:<10} -> {describe_day(d)}")
