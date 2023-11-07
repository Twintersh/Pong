todo_list = []

def addTask(task_name):
	todo_list.append({"task": task_name, "completed": False})
	print(f'task {task_name} added!')

def viewTasks():
	if todo_list:
		for index, task in enumerate(todo_list):
			status = "X" if task['completed'] else " " 
			print(f"{index + 1}-[{status}] {task['task']}")
	else:
		print("the list is empty.")

def completeTask(index):
	if 0 <= index < len(todo_list):
		todo_list[index]['completed'] = not todo_list[index]['completed']
		if todo_list[index]['completed'] == True:
			print(f"task {todo_list[index]['task']} checked.")
		else:
			print(f"task {todo_list[index]['task']} unchecked")
	else:
		print("invalid index.")
	
def removeTask(index):
	if 0 <= index < len(todo_list):
		task_name = todo_list[index]['task']
		del todo_list[index]
		print(f"task {task_name} deleted.")
	else:
		print("Invalid index")

while (1):
	print("What do you want to do?")
	print("1- add task")
	print("2- view tasks")
	print("3- complete task")
	print("4- delete task")
	print("5- exit")
	choice = input("\nmake a choice: ")

	if choice == "1":
		task = input("\nenter a task>> ")
		addTask(task)
		print("\n")
	elif choice == "2":
		viewTasks()
		print("\n")
	elif choice == "3":
		viewTasks()
		index = int(input("Choose the task you want to complete: ")) - 1
		completeTask(index)
		print("\n")
	elif choice == "4":
		viewTasks()
		index = int(input("Choose the task you want to delete: ")) - 1
		removeTask(index)
		print("\n")
	elif choice == "5" or choice == "exit":
		print("See you next time!")
		break
	else:
		print("Unrecognized response. Please enter a valid number.\n")
