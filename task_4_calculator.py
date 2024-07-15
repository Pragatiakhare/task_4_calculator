def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_operation():
    while True:
        operation = input("Choose operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Invalid operation! Please enter one of +, -, *, /.")

def calculator():
    print("Welcome to the Python Calculator!")
   
    while True:
        num1 = get_number("Enter first number: ")
        operation = get_operation()
        num2 = get_number("Enter second number: ")
       
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
       
        print(f"The result is: {result}")
       
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()