from task_manager import *

predefined_usernames = ["Illia", "Oksana", "Andrii"]
users = {name: User(name) for name in predefined_usernames}

program_is_work = True
print("Welcome to the Task Manager!")

def introduction():
    print("\n==============================")
    print("TASK MANAGER MENU")
    print("==============================")
    print("1 - Add a task")
    print("2 - Delete a task")
    print("3 - View tasks for a day")
    print("4 - Logout")
    print("==============================")

while program_is_work:
    name = input("\nEnter your name to login (or type 'quit' to exit): ")
    if name.lower() == "quit":
        break

    if name in users:
        current_user = users[name]
        print(f"Welcome back, {name}!")
    else:
        print("User not found. Access denied.")
        continue

    user_active = True
    while user_active:
        introduction()
        user_answer = input("Enter a number (1-4): ")

        if user_answer == "1":
            day = input("Enter a day: ")
            task = input("Enter task: ")
            current_user.add_task(day, task)
            print()

        elif user_answer == "2":
            day = input("Enter a day: ")
            task = input("Enter task to delete: ")
            current_user.delete_task(day, task)
            print()

        elif user_answer == "3":
            day = input("Enter a day: ")
            current_user.read_task(day)
            print()

        elif user_answer == "4":
            user_active = False
            print(f"Logged out from {current_user.name}.\n")

        else:
            print("Invalid option.\n")

print("Bye!")
