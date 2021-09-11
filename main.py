import PySimpleGUI as sg
from models.Container import Container
from models.Ports import Port
from layout import Layout

containers = []
ports = [Port("5000", "5000"), Port("5001", "5001")]
containers.append(Container("Raven", "raven", ports))
containers.append(Container("redis", "redis", ports))
containers.append(Container("mongoDb", "mongo", ports))

sg.theme('DarkTanBlue')

menu = [
    [sg.Input(visible=False, key='-hiden-input-')],
    Layout.createContainersRow(containers),
    Layout.createElementsRow(),
    Layout.createImageSection(),
]

intput = [
    [
        sg.Text(auto_size_text=True, background_color='white', text_color='black', size=(200, 100), key="-input-")
    ]
]

app_layout = [
    [

        sg.Col(menu, pad=((20, 0), (150, 10)), expand_y=True, expand_x=True),
        sg.VSeparator(),
        sg.Column(intput)
    ]
]

window = sg.Window('Docker-Compose Generator', app_layout, size=(1200, 800),
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
activeContainer = Container(None, None, None)
while True:
    event, values = window.read()
    window["-input-"].update(containers[0].name)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    Layout.setCurrentContainer(containers, event)
    if Layout.handleContainerControls(containers, event):
        Layout.toggleVisibilityOfSectionControls(window, True)
    if event == '-save-image-name-':
        Layout.updateContainerName(activeContainer, values['-image-name-value-'])
    if event == '-image-':
        Layout.toggleVisibilityOfSectionImage(window, True)

window.close()
