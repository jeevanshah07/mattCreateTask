def view(todo_list):
    # print a newline and then the border
    print("\n")
    print("#### TODO LIST ####")

    # iterate through the list and print out each item
    for i in range(len(todo_list)):
        display_item = "Item #" + str(i + 1) + ": " + todo_list[i]
        print(display_item)

    # finish the border and add a newline
    print("#### #### #### ####")
    print("\n")
        

def add(todo_list):
    # initiate variables for inputted description and date
    new_item_desc = input("Enter the description for your task: ")
    new_item_date = input("Enter the date the task needs to be completed: ")

    # create new item
    new_item = new_item_desc + " (Due: " + new_item_date + ")"

    # add new item to list
    todo_list.append(new_item)

    return todo_list

def remove(todo_list):
    # display the list
    view(todo_list)

    # collect item number and subtract one to get index
    index = int(input("Enter the # of the item to be removed: ")) - 1

    # check that index is value
    if index < len(todo_list):
        item = todo_list[index]  # find item in list
        todo_list.remove(item)  # remove the item from the todo_list
    else: 
        print("Invalid index!")


def check_off(todo_list):
    # display todo list and collect index
    view(todo_list)
    index = int(input("Enter the # of the item to be checked off: ")) - 1

    # ensure validity
    if index < len(todo_list):
        todo_list[index] = todo_list[index] + " - DONE"  # add indicator that item is done
    else:
        print("Invalid index!")

    return todo_list

def create_menu(todo_list):
    # Check if todo_list is empty
    # Or, equiventally, check if it's the first time the program is being run

    run = True
    while run:
        # initiate our program loop
        if len(todo_list) > 0:
            # print out our menu
            print("Select from the following options:")
            print("1. View todo list")
            print("2. Add to todo list")
            print("3. Remove from todo list")
            print("4. Check off an item")
            print("5. Exit")

            # take user input for selection, ensure that user input is a number
            try:
                menu_choice = int(input("Enter either 1, 2, 3, 4, or 5 for your selection: "))
            except ValueError:
                print("Invalid choice!\n")
                continue

            # check user input and call the respective function
            if menu_choice == 1:
                view(todo_list)
            elif menu_choice == 2:
                add(todo_list)
            elif menu_choice == 3:
                remove(todo_list)
            elif menu_choice == 4:
                check_off(todo_list) 
            elif menu_choice == 5:
                print("Bye!")
                run = False
            else:
                print("Invalid choice")
    else:
        # Print our welcome message
        print("Welcome to your todo list! Let's begin by adding an item!")
        todo_list = add(todo_list)  # add a new item to our todo list
        create_menu(todo_list)  # call create_menu again with our updated todo list



def main():
    todo_list = []
    create_menu(todo_list)


main()