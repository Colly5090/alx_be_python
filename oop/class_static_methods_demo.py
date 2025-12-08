#!/usr/bin/env python3

"""Class with Static and Class Methods Demo"""

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not access class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Uses cls to access class-level data."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
