#!/usr/bin/env python3


class BankAccount:
    """A simple bank account class"""

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.account_balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"

    def get_balance(self):
        """Return the current balance"""
        return f"Current balance: ${self.account_balance}"
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")