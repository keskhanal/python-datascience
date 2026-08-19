"""Magic (dunder) methods - making your objects behave like built-ins."""

class Money:
    def __init__(self, amount, currency="NPR"):
        self.amount = amount
        self.currency = currency

    def __str__(self):                    # print(obj) / str(obj)
        return f"{self.amount:.2f} {self.currency}"

    def __repr__(self):                   # what you see in the REPL / in a list
        return f"Money({self.amount!r}, {self.currency!r})"

    def __add__(self, other):             # obj + obj
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):              # obj == obj
        return (self.amount, self.currency) == (other.amount, other.currency)

    def __lt__(self, other):              # obj < obj  -> also enables sorted()
        return self.amount < other.amount


class Cart:
    def __init__(self, items=None):
        self.items = items or []

    def __len__(self):                    # len(obj)
        return len(self.items)

    def __getitem__(self, index):         # obj[i]  -> also makes it iterable
        return self.items[index]

    def __contains__(self, item):         # item in obj
        return item in self.items


a, b = Money(100), Money(250.5)
print(a, "+", b, "=", a + b)
print([a, b])                             # uses __repr__
print(a == Money(100), a < b)
print(sorted([b, a]))

cart = Cart(["apple", "banana"])
print(len(cart), cart[0], "apple" in cart)
for item in cart:
    print(" -", item)
