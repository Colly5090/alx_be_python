#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        sys.exit(1)

    # Support both "withdraw:50" and "withdraw 50"
    command = None
    amount = None

    if ":" in sys.argv[1]:
        command, amount_str = sys.argv[1].split(":")
        amount = float(amount_str)
    else:
        command = sys.argv[1]
        if len(sys.argv) > 2:
            amount = float(sys.argv[2])

    # Handle commands
    if command == "deposit" and amount is not None:
        print(account.deposit(amount))

    elif command == "withdraw" and amount is not None:
        print(account.withdraw(amount))

    elif command == "display":
        print(account.get_balance())

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
