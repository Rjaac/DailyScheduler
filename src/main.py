from task_manager import add_task, view_tasks, remove_task

def display_menu():
    print("\n--- Daily Scheduler ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to remove: "))
                remove_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting Daily Scheduler.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
