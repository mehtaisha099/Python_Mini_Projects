tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

            number = int(input("Enter task number to remove: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")