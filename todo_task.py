# This is my first tool to keep my python learning in high pace.
class Todo:
    tasks = []
    def add_task(self):
        task = input("Enter the Input")
        self.tasks.append(task)
        print(f"Task: {task} added")
    def delete_task(self):
        try:
            self.list_task()
            delete_task = int(input("Enter the task number to delete:"))-1
            self.tasks.pop(delete_task)
            print(f"Task number {delete_task} deleted")
        except Exception as e:
            print(f"Exception occured-{e}")

    def list_task(self):
        if not self.tasks:
            print("Tasks is empty")
        else:
            for id, value in enumerate(self.tasks,1):
                print(f"{id}. {value}")
    def list_last_added(self):
        if not self.tasks:
            print("Tasks are empty")
        else:
            print(f"Last added tasks is {self.tasks[-1]}")




def start():
    todo = Todo()
    while True:
        print("##############################")
        print("1. ADD TASK")
        print("2. DELETE TASK")
        print("3. LIST TASK")
        print("4. LAST ADDED TASK")
        print("5. EXIT")
        print("##############################")

        user_input = input("Enter the choice in TODO app")
        if user_input == "1":
            todo.add_task()
        elif user_input == "2":
            todo.delete_task()
        elif user_input == "3":
            todo.list_task()
        elif user_input == "4":
            todo.list_last_added()
        elif user_input == "5":
            print("Thanks for coming...")
            break
        else:
            print("Invalid input")

if __name__ == '__main__':
    start()