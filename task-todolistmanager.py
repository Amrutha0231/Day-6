todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, item in enumerate(todo_list, 1):
            status = " [x] " if item["completed"] else " [ ] "
            print(f"{index}.{status}{item['task']}")

def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(todo_list):
            todo_list[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def remove_completed_tasks():
    todo_list[:] = [task for task in todo_list if not task["completed"]]
    print("Completed tasks removed.")

while True:
    print("\nChoose an action:")
    print("1 - Add task")
    print("2 - View tasks")
    print("3 - Mark task as completed")
    print("4 - Remove completed tasks")
    print("5 - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        remove_completed_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
