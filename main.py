import PySimpleGUI as sg
import CipherC as Cipher

# key
from Container import Container
from Ports import Ports, Port

key = "DSckaLWVPK18MqaMjEVcnqScNBrQI2LHpvml6MtPosQ="
key = key.encode()
# Pattern
pattern = 3
encrypted = ""
decrypted = ""
text = ""
options = ""
orginal_text = ""

containers = []
ports = [Port("5000", "5000"), Port("5001", "5001")]
containers.append(Container("test1", "redis", ports))
containers.append(Container("test2", "mongo", ports))


def CheckRadioButtton():
    if values["-CE-"]:
        return "Cesar"
    if values["-FE-"]:
        return "Fernet"
    if values["-OT-"]:
        return "OneTime"


def appendButton(elements):
    array = []
    for container in elements:
        array.append(sg.Button(str(container.name)))
    return array


rowButtons = appendButton(containers)
container_name = [

]
file_browse = [
    rowButtons,
    [
        sg.Text("Choose elements"),
        sg.Button('Image', enable_events=True, key="-image-"),
        sg.Button('Build', enable_events=True, key="-build-"),
        sg.Button('Enviroments', enable_events=True, key="-env-"),
        sg.Button('Depends', enable_events=True, key="-depends-"),
    ],
    [
        sg.Text("Container name: ", key='-image-name-', visible=False),
        sg.In(size=(25, 1), enable_events=True,key='-image-name-value-', visible=False),
    ]
    ,
    [

        sg.In(size=(25, 1), enable_events=True, key='-SAVE_IN-', visible=False),
        sg.Button('Ok', enable_events=True, key='-SAVE_OK-', visible=False)
    ]
]
save_file = [
    [
        sg.Text("Choose File"),
        sg.In(size=(25, 1), enable_events=True),
        sg.FileBrowse(),
        sg.Button('Ok')
    ]
]
intput = [
    [
        sg.Text(auto_size_text=True, size=(40, 35), key="-TOIN-")
    ]
]
output = [
    [
        sg.Text(auto_size_text=True, size=(40, 35), key="-TOOT-")

    ]
]
layout = [
    [

        sg.Col(file_browse),
        sg.VSeparator(),
        sg.Column(intput),
        sg.VSeparator(),
        sg.Column(output),
    ]
]

window = sg.Window('Cesar Cipher', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == '-image-':
        window['-image-name-'].update(visible=True)
        window['-image-name-value-'].update(visible=True)
    else:
        window['-image-name-'].update(visible=False)
        window['-image-name-value-'].update(visible=False)


window.close()
