#!/usr/bin/env python3

"""Personal Daily Reminder"""

user_task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower();
time_bound = input("Is it time-bound? (yes/no): ").lower();

match priority:
    case "high":
        priority_msg = f"Reminder: '{user_task}' is a high priority task"
    case "medium":
        priority_msg = f"Reminder: '{user_task}' is a medium priority task"
    case "low":
        priority_msg = f"Reminder: '{user_task}' is a low priority task. Consider completing it when you have free time."
    case _:
        priority_msg = f"Reminder: '{user_task}' has an unknown priority level"

if time_bound == "yes":
    priority_msg += " that requires immediate attention today!"

print(priority_msg)