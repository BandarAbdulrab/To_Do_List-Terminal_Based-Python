from datetime import datetime, timedelta


# File paths for storing tasks
tasks_code_file = "Tasks File(Code Formated).txt"
tasks_readable_file = "Tasks File(Readable Formated).txt"


def load_tasks():
    tasks_list = []
    try:
        with open(tasks_code_file, 'r') as file:
            for line in file:
                description, times, deadline, priority, category, status = line.strip().split("|")
                task_dictionary = {
                    "description": description,
                    "times": times.split(","),
                    "deadline": deadline,
                    "priority": priority,
                    "category": category,
                    "status": status
                }
                tasks_list.append(task_dictionary)
    except FileNotFoundError:
        pass
    return tasks_list


def save_tasks(tasks_list):

    # Save in code format
    with open(tasks_code_file, 'w') as file:
        for task_dictionary in tasks_list:
            line = f"{task_dictionary['description']}|{','.join(task_dictionary['times'])}|{task_dictionary['deadline']}|{task_dictionary['priority']}|{task_dictionary['category']}|{task_dictionary['status']}\n"
            file.write(line)
    
    # Save in human-readable format
    with open(tasks_readable_file, 'w') as file:
        file.write("=== To-Do List ===\n")
        file.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for i, task_dictionary in enumerate(tasks_list, 1):
            file.write(f"Task {i}:\n")
            file.write(f"Description: {task_dictionary['description']}\n")
            file.write(f"Times: {', '.join(task_dictionary['times'])}\n")
            file.write(f"Deadline: {task_dictionary['deadline']}\n")
            file.write(f"Priority: {task_dictionary['priority']}\n")
            file.write(f"Category: {task_dictionary['category']}\n")
            file.write(f"Status: {task_dictionary['status']}\n")
            file.write("-" * 30 + "\n")


def add_task(tasks_list):
    description = input("Enter task description: ").strip()
    times = input("Enter times to do the task (e.g., 'Morning, Evening'): ").strip()
    deadline = input("Enter deadline (format: YYYY-MM-DD HH:MM): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip()
    category = input("Enter category (e.g., Work, Personal): ").strip()
    
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        task_dictionary = {
            "description": description,
            "times": [time.strip() for time in times.split(",")],
            "deadline": deadline_date.strftime("%Y-%m-%d %H:%M"),
            "priority": priority,
            "category": category,
            "status": "Not Started"  # Default status
        }
        tasks_list.append(task_dictionary)
        print("Task added successfully!")
    except ValueError:
        print("Invalid deadline format. Task not added.")


def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks available.")
        return
    
    for i, task_dictionary in enumerate(tasks_list, start=1):
        status = task_dictionary['status']
        deadline_date = datetime.strptime(task_dictionary['deadline'], "%Y-%m-%d %H:%M")
        today = datetime.now()

        if status != "Done":
            if deadline_date - today <= timedelta(days=1) and today < deadline_date:
                status += " - *Approaching Deadline*"
            elif today >= deadline_date:
                status += " - **Deadline Passed**"

        print(f"\nTask {i}:")
        print(f"  Description: {task_dictionary['description']}")
        print(f"  Times: {', '.join(task_dictionary['times'])}")
        print(f"  Deadline: {task_dictionary['deadline']}")
        print(f"  Priority: {task_dictionary['priority']}")
        print(f"  Category: {task_dictionary['category']}")
        print(f"  Status: {status}")


def delete_task(tasks_list):
    view_tasks(tasks_list)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks_list):
            tasks_list.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def edit_task(tasks_list):
    view_tasks(tasks_list)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks_list):
            print("Leave fields blank if no changes are needed.")
            description = input("Enter new description (or press Enter): ").strip()
            times = input("Enter new times (or press Enter): ").strip()
            deadline = input("Enter new deadline (YYYY-MM-DD HH:MM, or press Enter): ").strip()
            priority = input("Enter new priority (High/Medium/Low, or press Enter): ").strip()
            category = input("Enter new category (or press Enter): ").strip()
            status = input("Enter new status (Not Started/On Doing/Done, or press Enter): ").strip()

            if description:
                tasks_list[index]['description'] = description
            if times:
                tasks_list[index]['times'] = [time.strip() for time in times.split(",")]
            if deadline:
                try:
                    datetime.strptime(deadline, "%Y-%m-%d %H:%M")
                    tasks_list[index]['deadline'] = deadline
                except ValueError:
                    print("Invalid deadline format. Deadline not changed.")
            if priority:
                tasks_list[index]['priority'] = priority
            if category:
                tasks_list[index]['category'] = category
            if status:
                tasks_list[index]['status'] = status
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main_program_loop():
    tasks_list = load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        print("Note: You can view tasks in human-readable format in: Tasks File(Readable Formated).txt")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks_list)
        elif choice == '2':
            add_task(tasks_list)
            save_tasks(tasks_list)
        elif choice == '3':
            edit_task(tasks_list)
            save_tasks(tasks_list)
        elif choice == '4':
            delete_task(tasks_list)
            save_tasks(tasks_list)
        elif choice == '5':
            print("Goodbye! Thanks for using our program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_program_loop()
# Can be main_program_loop() only