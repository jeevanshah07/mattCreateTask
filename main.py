def view(todo_list):
    print("\n")
    print("#### TODO LIST #####")

    for i in range(len(todo_list)):
        print(f"Item #{i+1}: {todo_list[i]}")

    print("#### #### #### #####")
    print("\n")


def add(todo_list):
    new_item_desc = str(input("Enter the description for the task: "))
    new_item_date = str(
        input("Enter the date the task needs to be completed (DD/MM/YYYY): ")
    )

    new_item = f"{new_item_desc} (Due: {new_item_date})"
    todo_list.append(new_item)

    return todo_list


def remove(todo_list: list[str]):
    view(todo_list)
    index = int(input("Enter the # of the item to be removed: ")) - 1

    if index < len(todo_list):
        item = todo_list[index]
        todo_list.remove(item)
    else:
        print("Invalid index!")


def check_off(todo_list: list[str]):
    view(todo_list)
    index = int(input("Enter the # of the item to be checked off: ")) - 1

    if index < len(todo_list):
        todo_list[index] = f"{todo_list[index]} - DONE"
    else:
        print("Invalid index!")

    return todo_list


def create_menu(todo_list):
    if len(todo_list) > 0:
        while True:
            print(
                "Select from the following options: \n 1. View todo list \n 2. Add to todo list \n 3. Remove from todo list \n 4. Check off an item \n 5. Exit"
            )
            menu_choice = int(
                input("Enter either 1, 2, 3, or 4 for your selected option: ")
            )

            if menu_choice == 1:
                view(todo_list)
            elif menu_choice == 2:
                add(todo_list)
            elif menu_choice == 3:
                remove(todo_list)
            elif menu_choice == 4:
                todo_list = check_off(todo_list)
            elif menu_choice == 5:
                exit()
            else:
                print("Invalid choice!")
                create_menu(todo_list)
    else:
        print("Welcome to your todo list! Let's begin by adding an item!")
        todo_list = add(todo_list)
        create_menu(todo_list)


def main():
    todo_list = []
    create_menu(todo_list)


if __name__ == "__main__":
    main()
