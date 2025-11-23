#!/usr/bin/env python3

"""Arithmetic Operations Function"""

def perform_operation(num1, num2, operation):
    if operation == 'add':
       return num1 + num2
    elif operation == 'subtract':
       return num1 - num2
    elif operation == 'multiply':
       return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Can't divide by zero"
        return num1 / num2
    else:
        return "Select the correct operation for calculation"
