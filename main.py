import PySimpleGUI as sg
from models.Container import Container
from models.Ports import Port
from layout import Layout
from layout import MenuLayout as menuLayout

containers = []
ports = [Port("5000", "5000"), Port("5001", "5001")]
containers.append(Container("Raven"))
containers.append(Container("redis"))
containers.append(Container("mongoDb"))

sg.theme('DarkTanBlue')

menu = [
    [sg.Input(visible=False, key='-hiden-input-')],
    menuLayout.createContainersRow(containers),
    menuLayout.createElementsRow(),
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createImageSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-image-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0, ))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createBuildSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-build-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0, ))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createPortsSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-ports-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createEnvSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-env-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createDependsSection(), vertical_alignment='c', )]],
                     vertical_alignment='c', key='-depends-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0))],

]

intput = [
    [
        sg.Text(auto_size_text=True, size=(100, 200), key="-input-")
    ]
]

app_layout = [
    [

        sg.Col(menu, pad=((20, 0), (150, 0)), expand_y=True, expand_x=True),
        sg.VSeparator(),
        sg.Column(intput, pad=((20, 0), (150, 10)))
    ]
]

window = sg.Window('Docker-Compose Generator', app_layout, size=(1200, 800), resizable=True,
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
activeContainer = Container(None, None, None)
while True:
    event, values = window.read()
    window["-input-"].update(containers[0].name)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    currnetContainer = Layout.setCurrentContainer(containers, event)
    if Layout.handleContainerControls(containers, event):
        Layout.toggleVisibilityOfSectionControls(window, True)
    if event == '-save-image-':
        Layout.updateContainerName(activeContainer, values['-image-name-value-'])
    if event == '-image-':
        Layout.toggleVisibilityOfSectionImage(window, True)
    if event == '-build-':
        Layout.toggleVisibilityOfSectionBuild(window, True)
    if event == '-ports-':
        Layout.toggleVisibilityOfSectionPort(window, True)
    if event == '-env-':
        Layout.toggleVisibilityOfSectionEnv(window, True)
    if event == '-depends-':
        Layout.toggleVisibilityOfSectionDepends(window, True)

window.close()
