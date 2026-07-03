print("Welcome to the Python TO-DO list generator")

list = []
while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Show Task")
    print("4. Exit")

    choice = int(
        input("Enter your choice according to the above information: "))

    if choice == 1:
        task = input("Enter task: ")
        list.append(task)

    elif choice == 2:
        i = int(input("Which task do you want to remove?: "))
        list.remove(list[i])

    elif choice == 3:
        print(list)

    elif choice == 4:
        break
    else:
        break
