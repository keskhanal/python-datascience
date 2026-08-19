"""Exercise solution: guess the secret number (scripted, no input needed)."""

secret = 7
guesses = [3, 9, 6, 7]          # pretend these came from input()

for attempt, guess in enumerate(guesses, start=1):
    if guess < secret:
        print(f"Attempt {attempt}: {guess} is too low")
    elif guess > secret:
        print(f"Attempt {attempt}: {guess} is too high")
    else:
        print(f"Attempt {attempt}: correct! The number was {secret}")
        break
else:
    print("Out of guesses!")
