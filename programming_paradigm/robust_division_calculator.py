#!/usr/bin/env python3
"""Robust Division Calculator with Error Handling"""

def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""

    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
