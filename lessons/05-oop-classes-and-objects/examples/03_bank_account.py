"""A realistic class: state that changes over time, guarded by methods."""

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: balance is {self.balance}")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def statement(self):
        print(f"\nStatement for {self.owner}")
        for kind, amount in self.transactions:
            print(f"  {kind:<9} {amount:>8.2f}")
        print(f"  {'balance':<9} {self.balance:>8.2f}")


if __name__ == "__main__":
    acc = BankAccount("Bibek", 1000)
    acc.deposit(500)
    acc.withdraw(200)

    try:
        acc.withdraw(10_000)
    except ValueError as e:
        print("Rejected:", e)

    acc.statement()
