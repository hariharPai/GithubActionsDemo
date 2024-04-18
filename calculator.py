import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

if len(sys.argv) != 4:
    print("Usage: python calculator.py operation num1 num2")
    sys.exit(1)

operation = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if operation == 'add':
    result = add(num1, num2)
elif operation == 'subtract':
    result = subtract(num1, num2)
elif operation == 'multiply':
    result = multiply(num1, num2)
elif operation == 'divide':
    result = divide(num1, num2)
else:
    print("Invalid operation")
    sys.exit(1)

print(result)
