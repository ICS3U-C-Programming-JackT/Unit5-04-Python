#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 7th, 2025

# Calculator program in python


# Function to add
def add(n1, n2):
    print(n1, "+", n2, " = ", n1 + n2)


# Function to subtract
def subtract(n1, n2):
    print(n1, "-", n2, " = ", n1 - n2)


# Function to multiply
def multiply(n1, n2):
    print(n1, "*", n2, " = ", n1 * n2)


# Function to divide
def divide(n1, n2):
    if n2 == 0.0:
        print(n1, "/", n2, " = ", "Undefined")
    else:
        print(n1, "/", n2, " = ", n1 / n2)


# Function to handle inputs and call calculation functions
def main():

    # Get user input
    operation = input("Enter an operation to calculate (+,-,*,/): ")
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")

    # Try catch to prevent errors
    try:
        number1 = float(number1)
        number2 = float(number2)

        # Check operation input and call functions accordingly
        if operation == "+":
            add(number1, number2)
        elif operation == "-":
            subtract(number1, number2)
        elif operation == "*":
            multiply(number1, number2)
        elif operation == "/":
            divide(number1, number2)
        else:
            print("You didn't enter a proper operation!")

    except:

        # Error message:
        print("Error: either", number1, "or", number2, "is string.")


if __name__ == "__main__":
    main()
