import json
def load_todo_list():
    try:
        with open('todo_list.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_todo_list(todo_list):
    with open('todo_list.json', 'w') as file:
        json.dump(todo_list, file)
def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['title']} - {'Done' if task['completed'] else 'Not Done'}")
def add_task(todo_list, title):
    todo_list.append({'title': title, 'completed': False})
def mark_completed(todo_list, index):
    if 0 < index <= len(todo_list):
        todo_list[index - 1]['completed'] = True
def remove_task(todo_list, index):
    if 0 < index <= len(todo_list):
        del todo_list[index - 1]
def hello():
    todo_list = load_todo_list()
    while True:
        print("\n===== To-Do List =====")
        display_todo_list(todo_list)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            add_task(todo_list, title)
        elif choice == '2':
            index = int(input("Enter task index to remove: "))
            remove_task(todo_list, index)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            mark_completed(todo_list, index)
        elif choice == '4':
            save_todo_list(todo_list)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

hello()
