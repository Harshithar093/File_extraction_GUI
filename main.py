# from functions import get_todos,write_todos
#
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")  # inbuilt strftime(stringformat time) method from time module to print time
print("It is", now)

while True:
    user_input = input("enter the todo list option, add,edit,exit,show,complete: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        # todo = input("enter the todo items: ") + "\n"
        todo = user_input[4:]  # now we can just type add followed by the item to add in todo instead of input()

        # with open("todo.txt", "r") as file:
        #     todos = file.readlines()
        todos = functions.get_todos()  # call the function todos  instead of opening file and reading and assign it to variable todo

        todos.append(todo + "\n")
        functions.write_todos(todos)

        # with open("todo.txt", "w") as file:
        #     file.writelines(todos)

    elif user_input.startswith("show"):
        todos = functions.get_todos()

        # todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_input.startswith("edit"):
        try:

            user_edit = int(user_input[5:])
            user_edit = user_edit - 1

            todos = functions.get_todos()
            print("The existing todo items are:", todos)

            new_value = input("enter the value for new item: ")
            todos[user_edit] = new_value + "\n"

            functions.write_todos(todos)

            print("the edited value of todos list:", todos)

        except ValueError:
            print("The command is not valid")
            continue  # will take u back to user_input when there is value error

    elif user_input.startswith("complete"):
        try:
            user_remove = int(user_input[9:])
            user_remove = user_remove - 1

            todos = functions.get_todos()

            print("the todo items before deleting:", todos)
            todos_to_remove = todos[user_remove]
            todos.pop(user_remove)

            functions.write_todos(todos)

            message = f"Todo {todos_to_remove} was removed from the list"
            print(message)
            print("The todo list after removing item: ", todos)
        except IndexError:
            print("Index out of range in list")
    elif user_input.startswith("exit"):
        break
    else:
        print("command not valid")
print("bye")
