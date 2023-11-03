todo_list = []

def addTask(task_name):
	todo_list.append({"task": task_name, "completed": False})
	print(f'task {task_name} added!\n')

def viewTasks():
	if todo_list:
		for index, task in enumerate(todo_list):
			status = "X" if task['completed'] else " " 
			print(f"{index + 1}-[{status}] {task['task']}")
	else:
		print("the list is empty")
	print("\n");

# def completeTask()

while (1):
	print("What do you want to do?")
	print("1- add task")
	print("2- view tasks")
	print("5- exit")
	choice = input("\nmake a choice: ")

	if choice == "1":
		task = input("\nenter a task >> ")
		addTask(task)
	elif choice == "2":
		viewTasks()
	elif choice == "5" or choice == "exit":
		print("See you next time!")
		break
	else:
		print("Unrecognized response. Please enter a valid number.\n")
