"""Worked solutions for the lesson 03 exercises."""

# 1. Reverse the words in a sentence
sentence = "python is really fun"
print(" ".join(sentence.split()[::-1]))

# 2. Palindrome check (case-insensitive), slicing version
def is_palindrome(word: str) -> bool:
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# 3. Palindrome check with a loop
def is_palindrome_loop(word: str) -> bool:
    cleaned = word.lower().replace(" ", "")
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

for w in ["Madam", "Nurses run", "python"]:
    print(w, is_palindrome(w), is_palindrome_loop(w))

# 4. Prime check
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print([n for n in range(1, 30) if is_prime(n)])

# 5. Character frequency using a dictionary
word = "programming"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
