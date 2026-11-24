import json
from datetime import datetime


# LOAD TASKS FROM JSON FILE
with open("tasks.json", "r") as file:
    tasks = json.load(file)


# ADD TASK FUNCTION
def add_task():
    title = input("Enter task title: ")

    while True:
        description = input("Enter task description: ")

        if description.strip() == "":
            print("Description cannot be empty.")
            continue

        if description.strip().isdigit():
            print("Description cannot contain only numbers.")
            continue

        break

    new_task = {
    "title": title,
    "description": description,
    "completed": False,
    "priority": "Medium",
    "due_date": None
}

    

    tasks.append(new_task)

    print("Task added successfully!")


name = input("Please enter your name for record purpose: ")
print()
print(f"Hello {name}, is good to have you here. ")
print()


def view_pending_tasks():
    print("\n==== PENDING TASKS ====")

    for task in tasks:
        if not task["completed"]:
            print("Title:", task["title"])
            print("Description:", task["description"])
            print()


def view_completed_tasks():
    print("\n==== COMPLETED TASKS ====")

    for task in tasks:
        if task["completed"]:
            print("Title:", task["title"])
            print("Description:", task["description"])
            print()

def mark_task_completed():
    title = input("Enter the task title to mark as completed: ")
    found = False

    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            found = True
            print("Task marked as completed!")
    if not found:
        print("Task not found.")
        print()

def edit_task():
    title = input("Enter the task title you want to edit: ").strip()
    found = False

    for task in tasks:
        if task["title"].strip().lower() == title.lower():
            found = True

            print("1. Edit title")
            print("2. Edit description")

            choice = input("Choose what to edit: ")

            if choice == "1":
                new_title = input("Enter new title: ").strip()

                if new_title == "":
                    print("Title cannot be empty.")
                else:
                    task["title"] = new_title
                    print("Title updated successfully!")

            elif choice == "2":
                new_description = input("Enter new description: ").strip()

                if new_description == "":
                    print("Description cannot be empty.")
                elif new_description.isdigit():
                    print("Description cannot contain only numbers.")
                else:
                    task["description"] = new_description
                    print("Description updated successfully!")
                    print()

            else:
                print("Invalid choice.")

            break

    if not found:
        print("Task not found.")
        print()

def delete_task():
    title = input("Enter the task title you want to delete: ")
    found = False

    for task in tasks:
        if task["title"].lower() == title.lower():
            tasks.remove(task)
            found = True
            print("Task deleted successfully!")
            break

    if not found:
        print("Task not found.")
        print()

def assign_priority():
    title = input("Enter the task title: ")
    found = False

    for task in tasks:
        if task["title"].lower() == title.lower():
            found = True

            print("1. High")
            print("2. Medium")
            print("3. Low")

            choice = input("Choose priority: ")

            if choice == "1":
                task["priority"] = "High"
            elif choice == "2":
                task["priority"] = "Medium"
            elif choice == "3":
                task["priority"] = "Low"
            else:
                print("Invalid choice.")
                break

            print("Priority assigned successfully!")
            break

    if not found:
        print("Task not found.")
        print()

def add_due_date():
    title = input("Enter the task title: ")
    found = False

    for task in tasks:
        if task["title"].lower() == title.lower():
            found = True

            while True:
                due_date = input("Enter due date (YYYY-MM-DD): ")

                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    task["due_date"] = due_date
                    print("Due date added successfully!")
                    break

                except ValueError:
                    print("Invalid date. Use YYYY-MM-DD.")

            break

    if not found:
        print("Task not found.")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully!")

def load_tasks():
    global tasks

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    print("Tasks loaded successfully!")

    print()

def search_task():
    title = input("Enter the task title you want to search for: ").strip()
    found = False

    for task in tasks:
        if task["title"].lower() == title.lower():
            found = True

            print("\n==== TASK FOUND ====")
            print("Title:", task["title"])
            print("Description:", task["description"])
            print("Status:", "Completed" if task["completed"] else "Pending")
            print("Priority:", task["priority"])
            print("Due Date:", task["due_date"])
            print()

            break

    if not found:
        print("Task not found.")
        print()


# MENU
print()
while True:
    print("====TO-DO LIST====")
    print("1. Add Task")
    print("2. View pending task")
    print("3. View completed task")
    print("4. Mark task as completed")
    print("5. Edit task")
    print("6. Delete task")
    print("7. Assign priority")
    print("8. Add due dates")
    print("9. Save task")
    print("10. Load task")
    print("11. Exit")
    print("12. Search for a task")
    print()

    choice = input("Pick your choice: ").strip()

    print("You selected:", choice)

    if choice == "1":
        add_task()

    elif choice == "2":
        view_pending_tasks()

    elif choice == "3":
        view_completed_tasks()

    elif choice == "4":
        mark_task_completed()

    elif choice == "5":
        print("Edit task function is running")
        edit_task()
    
    elif choice == "6":
        delete_task()

    elif choice == "7":
        assign_priority()

    elif choice == "8":
        add_due_date()

    elif choice == "9":
        save_tasks()

    elif choice == "10":
        load_tasks()

    elif choice == "11":
        save_tasks()
        print(f"Thank you {name} for using the To-Do CLI Application. Goodbye!")
        break

    elif choice == "12":
        search_task()

    else:
        print("Invalid choice. Please choose between 1 and 12.")

    