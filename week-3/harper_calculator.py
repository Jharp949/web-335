"""
    Title: harper_calculator.py
    Author: James Harper
    Date: 27 August 2023
    Description: Variables and Functions in Python.
"""
#Variables for each parameter within the function
num1 = 14
num2 = 7
#Function adds num1 and num2
def add(num1, num2):
    return num1 + num2
#Function subtracts num1 and num2
def subtract(num1, num2):
    return num1 - num2
#Function divides num1 and num2
def divide(num1, num2):
    return num1 / num2
#Function multiplies num1 and num2
def multiply(num1, num2):
    return num1 * num2
#Variables which hold the concatenated values of num1, num2, and the result of each prior function
sum = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
difference = str(num1) + " + " + str(num2) + " is " + str(subtract(num1, num2))
quotient = str(num1) + " + " + str(num2) + " is " + str(divide(num1, num2))
product = str(num1) + " + " + str(num2) + " is " + str(multiply(num1, num2))
#prints each variable to the console
print(sum)
print(difference)
print(quotient)
print(product)
