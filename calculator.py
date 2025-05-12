#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 7th, 2025

# Calculator program in python

# Function to add
def calculate(sign,first_number,second_number):
    if sign == "+":
        return first_number + second_number
    if sign == "-":
        return first_number - second_number
    if sign == "*":
        return first_number * second_number
    if sign == "/":
        return first_number / second_number
    if sign == "%":
        return first_number % second_number

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
        if operation in "+-*/%":
            if operation in "/%" and number2 == 0:
                print(number1,operation,number2,"= Undefined")
            else:
                result = calculate(operation,number1,number2)
                print(number1,operation,number2,"=",result)
        else:
            print("You didn't enter a proper operation!")

    except:
        # Error message:
        print("Error: either", number1, "or", number2, "is not a valid number.")

if __name__ == "__main__":
    main()
