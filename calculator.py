# Simple Calculator Program
# This program performs basic arithmetic operations
# It takes two numbers and an operation as input from the user. Then it performs the operation and prints the result.

num = input("Enter a number: ")
num2 =input("Enter another number: ")
operation = input("Enter an operation (+, -, *, /): ")

num = float(num)
num2 = float(num2)

try:
    if operation == '+':
        result = num + num2
    elif operation == '-':
        result = num - num2
    elif operation == '*':
        result = num * num2
    elif operation == '/':
        result = num / num2
    else:
        print("Invalid operation")
        result = None
    if result is not None:
        print("Result:", result)
except Exception as e:
    print("An error occurred:", e)
    

