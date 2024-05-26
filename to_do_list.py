import os

# Define a list to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTo-Do List Manager")
    print("==================")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. View tasks")
    print("4. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print(f'Task "{task}" added!')

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]['completed'] = True
            print(f'Task "{tasks[task_number]["task"]}" marked as completed!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index}. {task['task']} - {status}")

# Main function to run the application
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_completed()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
