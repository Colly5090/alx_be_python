#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def main():
    # Starting balance (example)
    account = BankAccount(100)

    # No command provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount
    parts = sys.argv[1].split(":")
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 else None

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
