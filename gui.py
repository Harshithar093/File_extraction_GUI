import functions
import PySimpleGUI as sg

label = sg.Text("To Do list")
input_box = sg.InputText(tooltip="Enter to do")
add_Button = sg.Button("Add")


window = sg.Window('My To Do App',
                   layout=[[label], [input_box], [add_Button]])
window.read()
window.close()
