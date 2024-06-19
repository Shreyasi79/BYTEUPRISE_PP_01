def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(tasks):
    if not tasks:
        print("\nNo tasks to remove.")
        return

    view_tasks(tasks)
    task_num = int(input("\nEnter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
