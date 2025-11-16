#Personal Daily Reminder. This app reminds the user about a single, priority task for the day based on time sensitivity.

#Step 1: Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ") 

#Step 2: Process the task based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

#Step 3: Provide a customized reminder    
if time_bound == "yes":
    message += " that requires immediate attention today!"
    print("Reminder:", message)
else:
    print(f"\nNote: {message}. Consider completing it when you have free time.")
