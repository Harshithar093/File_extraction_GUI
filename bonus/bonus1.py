import PySimpleGUI as ps
from zip_creator import make_archive

ps.theme("Black")
label1 = ps.Text("Select files to compress:")
input_box1 = ps.Input()
input_Button1 = ps.FilesBrowse("choose",key="files")

label2 = ps.Text("Select destination folder:")
input_box2 = ps.InputText()
input_Button2 = ps.FolderBrowse("choose", key="folder")

main_button = ps.Button("Compress")
output_label = ps.Text(key='output')

window = ps.Window('File Zipper',
                   layout=[[label1, input_box1, input_Button1],
                           [label2, input_box2, input_Button2],
                           [main_button,output_label]])
while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";") #to seperate the files
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed")
window.close()
