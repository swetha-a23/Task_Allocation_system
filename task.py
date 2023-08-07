class Task:
    def __init__(self, name, details, assigned_to):
        self._name = name
        self._details = details
        self._assigned_to = assigned_to

    def display_details(self):
        print("Name:", self._name)
        print("Details:", self._details)
        print("Assigned to:", self._assigned_to)
        print()

    def get_name(self):
        return self._name

    def get_details(self):
        return self._details

    def get_assigned_to(self):
        return self._assigned_to

    def set_name(self, name):
        self._name = name

    def set_details(self, details):
        self._details = details

    def set_assigned_to(self, assigned_to):
        self._assigned_to = assigned_to


class TaskManager:
    def __init__(self):
        self._tasks = []

    def create_task(self):
        name = input("Enter task name: ")
        details = input("Enter task details: ")
        assigned_to = input("Enter team member name to assign task to: ")
        task = Task(name, details, assigned_to)
        self._tasks.append(task)
        print("Task created successfully.")

    def read_tasks(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self._tasks):
                print(f"Task {i+1}:")
                task.display_details()

    def update_task(self):
        task_index = int(input("Enter task number to update: ")) - 1
        if task_index < 0 or task_index >= len(self._tasks):
            print("Invalid task number.")
            return

        task = self._tasks[task_index]
        print("Current Task Details:")
        task.display_details()

        name = input("Enter new task name: ")
        details = input("Enter new task details: ")
        assigned_to = input("Enter new team member name to assign task to: ")

        task.set_name(name)
        task.set_details(details)
        task.set_assigned_to(assigned_to)

        print("Task updated successfully.")

    def delete_task(self):
        task_index = int(input("Enter task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(self._tasks):
            print("Invalid task number.")
        else:
            del self._tasks[task_index]
            print("Task deleted successfully.")

    def menu(self):
        print("Task Allocation System")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def run(self):
        while True:
            try:
                self.menu()
                choice = int(input("Enter action to be performed: "))

                if choice == 1:
                    self.create_task()
                elif choice == 2:
                    self.read_tasks()
                elif choice == 3:
                    self.update_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")




task_manager = TaskManager()
task_manager.run()
