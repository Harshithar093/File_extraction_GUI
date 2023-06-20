FILEPATH = "todo.txt"


def get_todos(filename=FILEPATH):
    """ Read a text file and return the list of to-do items
    """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":  # it nly executes when we run functions file, hee name of teh file  is main
    print(get_todos())
