## task list ##

user_choice = -1

tasks = []


def show_tasks():
    task_index = 1
    for task in tasks:
        print(f" nb {task_index} : {task}")
        task_index += 1


def add_task():
    task = input("add your task")
    tasks.append(task)
    print("task ")


def delete_task():
    task_index = int(input("number of task to delete")) - 1
    if task_index < 1 or task_index > len(tasks):
        print("wrong index number")
        return
    tasks.pop(task_index)
    print("your importend task was removed")


def safe_to_file():
    file = open("task.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()


def load_tasks():
    try:
        file = open("task.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        print("not txt flie find")
        return


load_tasks()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()
    if user_choice == 4:
        safe_to_file()

    print("1:show tasks")
    print("2:add task")
    print("3:remove tasks")
    print("4:save to txt file")
    print("5:exit")

    user_choice = int(input(" your number choice : >>>"))
