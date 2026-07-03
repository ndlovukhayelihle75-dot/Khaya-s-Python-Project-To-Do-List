todo = ["Do homework", "Clean the house"]

while True:
    print("To-Do List:", todo)

    choice = input("Type add, remove, or exit: ")

    if choice == "add":
        item = input("Enter item: ")
        todo.append(item)

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in todo:
            todo.remove(item)

    elif choice == "exit":
        break