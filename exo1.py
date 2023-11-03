tasks = []

def addTask(task_name):
	tasks.append({"task": task_name, "completed": False})
	print(f'task {task_name} added!\n')

def viewTasks():
	if tasks:
		
	else:
		print("the list is empty")

while (1):
	print("What do you want to do? ")
	print("1- add task ")
	
	choice = input("make a choice: ")

	if choice == "1":
		task = input("enter a task ")
		addTask(task)
	else:
		print("à la prochaine sale dogo")
		break
