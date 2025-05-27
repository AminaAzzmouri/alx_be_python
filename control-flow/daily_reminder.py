# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate customized reminder
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unrecognized priority level"

# Check time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    # For non-time-bound tasks, add a friendly suggestion
    message += ". Consider completing it when you have free time."

# Print final reminder
print(message)
