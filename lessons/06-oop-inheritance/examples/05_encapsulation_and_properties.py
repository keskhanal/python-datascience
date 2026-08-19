"""Encapsulation: public, _protected and __private, plus @property."""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self._bank = "Vrit Bank"      # _protected: "internal, please don't touch"
        self.__balance = balance      # __private: name-mangled by Python

    # A read-only computed attribute
    @property
    def balance(self):
        return self.__balance

    @property
    def is_overdrawn(self):
        return self.__balance < 0

    def deposit(self, amount):
        self.__balance += amount


acc = Account("Bibek", 500)
print(acc.owner, acc.balance)          # called like an attribute, no ()
acc.deposit(250)
print(acc.balance, acc.is_overdrawn)

# You cannot assign to a property without a setter
try:
    acc.balance = 1_000_000
except AttributeError as e:
    print("Blocked:", e)

# __balance is name-mangled, not truly hidden - Python trusts the programmer
print(acc._Account__balance)


class Temperature:
    """A property WITH a setter, so assignment can be validated."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius, t.fahrenheit)
t.celsius = 100
print(t.celsius, t.fahrenheit)
try:
    t.celsius = -300
except ValueError as e:
    print("Rejected:", e)
