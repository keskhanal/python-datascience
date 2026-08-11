# from calculator.calculator import Calculator
# from calculator.message import greeting
from calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    a = 10
    b = 5

    # print(greeting("Alice"))
    add_result = calc.add(a, b)
    print(f"Addition: {a} + {b} = {add_result}")

    # print(f"Addition: {a} + {b} = {calc.add(a, b)}")
    # print(f"Subtraction: {a} - {b} = {calc.subtract(a, b)}")
    # print(f"Multiplication: {a} * {b} = {calc.multiply(a, b)}")
    # print(f"Division: {a} / {b} = {calc.divide(a, b)}")