def sum_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    
    return a / b

if __name__ == "__main__":
    num1 = 5
    num2 = 10
    sum_result = sum_two_numbers(num1, num2)
    mult_result = multiply_two_numbers(num1, num2)
    print(f"Sum: {sum_result}, Product: {mult_result}")
    print("Maths module loaded successfully.")
