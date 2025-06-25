import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Empty task not added.")

def update_task(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks[task_num - 1] = new_task
                save_tasks(tasks)
                print("Task updated.")
            else:
                print("Empty input. Task not updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted: {deleted}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()

