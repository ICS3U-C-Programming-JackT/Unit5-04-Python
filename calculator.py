#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 7th, 2025

# Calculator program in python

# Function to add
def add(n1, n2):
    return n1 + n2

# Function to subtract
def subtract(n1, n2):
    return n1 - n2

# Function to multiply
def multiply(n1, n2):
    return n1 * n2

# Function to divide
def divide(n1, n2):
    if n2 == 0.0:
        return "Undefined"
    else:
        return n1 / n2

# Function for modulo
def modulo(n1, n2):
    if n2 == 0.0:
        return "Undefined"
    else:
        return n1 % n2

# Function to handle inputs and call calculation functions
def main():

    # Get user input
    operation = input("Enter an operation to calculate (+,-,*,/,%): ")
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")

    # Try/catch to prevent errors
    try:
        number1 = float(number1)
        number2 = float(number2)

        # Determine which operation to perform
        if operation == "+":
            result = add(number1, number2)
        elif operation == "-":
            result = subtract(number1, number2)
        elif operation == "*":
            result = multiply(number1, number2)
        elif operation == "/":
            result = divide(number1, number2)
        elif operation == "%":
            result = modulo(number1, number2)
        else:
            print("You didn't enter a proper operation!")
            return

        # Print result from main
        if result == "Undefined":
            print("Result: Undefined")
        else:
            print("Result:", result)

    except:
        # Error message:
        print("Error: either", number1, "or", number2, "is not a valid number.")

if __name__ == "__main__":
    main()
