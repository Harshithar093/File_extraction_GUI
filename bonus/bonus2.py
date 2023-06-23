import PySimpleGUI as ps
from zip_extractor import archive_extract

ps.theme("Black")
label1 = ps.Text("Select archive:")
input_box1 = ps.Input()
input_Button1 = ps.FileBrowse("choose",key="archive")

label2 = ps.Text("Select dest dir:")
input_box2 = ps.InputText()
input_Button2 = ps.FolderBrowse("choose", key="folder")

main_button = ps.Button("Extract")
output_label = ps.Text(key='output', text_color="green")

window = ps.Window('Archive Extractor',
                   layout=[[label1, input_box1, input_Button1],
                           [label2, input_box2, input_Button2],
                           [main_button,output_label]])
while True:
    event, values = window.read()
    print(event,values)
    archivepath=values['archive']
    dest_dir=values['folder']
    archive_extract(archivepath,dest_dir)
    window['output'].update(value="Extraction Completed")
window.close()
