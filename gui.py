import functions
import PySimpleGUI as sg
import time

sg.theme("Black")
clock=sg.Text('',key='clock')
label = sg.Text("To Do list")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_Button = sg.Button("Add")

'''List box to show up which item of to-do list to edit '''
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events='True', size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To Do App',
                   layout=[[clock],
                        [label],
                           [input_box, add_Button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # which value to edit from todos key listbox
                new_todo = values['todo']  # enter the new value to be added

                todos = functions.get_todos()  # read the todos file
                index = todos.index(todo_to_edit)  # get the index value of edit item
                todos[index] = new_todo  # assign the index with value
                functions.write_todos(todos)  # write to file
                window['todos'].update(values=todos)  # to update windows list
            except IndexError:
                sg.popup("Please select the item first.", font=("Helvetica", 20))

        case "Complete":
            try:
                todos_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todos'].update(value='')
            except IndexError:
                sg.popup("Please select the item first.", font=("Helvetica", 20))
        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
window.close()
