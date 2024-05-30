tasks = []

def add_task(task):
    print(f"Task Name: {task}")
    print("Planning")
    print("In Progress")
    print("Completed")
    tasks.append(task)

if __name__ == "__main__":
    print("This is a to-do list")

    while True:
        print("\n.......................")
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")
        print(".......................")

        choice = input("What's your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            print("Your tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        elif choice == "3":
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")
