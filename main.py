import PySimpleGUI as sg
from Container import Container
from Ports import Port

containers = []
ports = [Port("5000", "5000"), Port("5001", "5001")]
containers.append(Container("Raven", "mongo", ports))
containers.append(Container("redis", "redis", ports))
containers.append(Container("mongoDb", "mongo", ports))


def CheckRadioButtton():
    if values["-CE-"]:
        return "Cesar"
    if values["-FE-"]:
        return "Fernet"
    if values["-OT-"]:
        return "OneTime"


def appendButton(elements):
    array = [sg.Text("Containers: ", key='-container-text-')]
    for container in elements:
        array.append(sg.Button(container.name, enable_events=True, key=f'-{container.name}-'))
    return array


sg.theme('DarkTanBlue')
rowButtons = appendButton(containers)
file_browse = [

    [sg.Input(visible=False)],

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
        sg.In(size=(25, 1), enable_events=True, key='-image-name-value-', visible=False),
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
        sg.Text(auto_size_text=True, size=(40, 35), key="-TOOT-", visible=True)

    ]
]
layout = [
    [

        sg.Col(file_browse, pad=((50, 0), 200), expand_y=True),
        sg.VSeparator(),
        sg.Column(intput)
    ]
]

window = sg.Window('Docker-Compose Generator', layout, size=(1200, 800), right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
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
