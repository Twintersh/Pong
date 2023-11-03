# Initialize an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task {task} added to the to-do list.")

# Function to view all tasks
def view_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list)
            status = "X" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")
    else:
        print("No tasks in the to-do list.")

# Function to mark a task as completed
def complete_task(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print(f"Task '{todo_list[index]['task']}' marked as completed.")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(index):
    if 0 <= index < len(todo_list):
        task_name = todo_list[index]["task"]
        del todo_list[index]
        print(f"Task '{task_name}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter the task number to mark as completed: ")) - 1
        complete_task(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Enter the task number to remove: ")) - 1
        remove_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

