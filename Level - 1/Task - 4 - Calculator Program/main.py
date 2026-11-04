print("Welcome to the Calculator Program")

a = float(input("Please enter a number: "))

operation = input("Please enter operation (+, -, *, /, %): ")

b = float(input("Please enter another number: "))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Cannot calculate modulus with zero"
    return a % b


if operation == "+":
    result = add(a, b)

elif operation == "-":
    result = subtract(a, b)

elif operation == "*":
    result = multiply(a, b)

elif operation == "/":
    result = divide(a, b)

elif operation == "%":
    result = modulus(a, b)

else:
    result = "Invalid operation"

print("Result:", result)
