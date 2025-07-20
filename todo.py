#TODO_LIST

# Store tasks in a list
tasks = []

def show_menu():
    print( TO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("hey Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("done  Task added!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "done"if task["done"] else "not done"
        print(f"{i}. {task['task']} {status}")

def mark_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print(" Task is done")
            else:
                print("Invalid number.")
        except:
            print("Please enter a number.")

# Start the app
while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        print("Goodbye, Manasvi!")
        break
    else:
        print("Invalid option. Try again.")
