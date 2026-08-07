def sum_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b


if __name__ == "__main__":
    num1 = 5
    num2 = 10
    sum_result = sum_two_numbers(num1, num2)
    mult_result = multiply_two_numbers(num1, num2)
    print(f"Sum: {sum_result}, Product: {mult_result}")