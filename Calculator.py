# Input to perform addition
def add(x, y):
    return x + y
# Input to perform subtraction
def subtract(x, y):
    return x - y
# Input to perform multiplication
def multiply(x, y):
    return x * y
# Input to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Main calculator function
def calculator():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter operation (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
        else:
            print("Invalid input. Please select a valid operation (1/2/3/4).")
    else:
        print("Invalid input. Please select a valid operation (1/2/3/4).")
# Run Calculator
calculator()