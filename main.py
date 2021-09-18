import PySimpleGUI as sg
from GeneratorHelper import Generator
from models.Container import Container
from models.Ports import Port
from layout import Layout, MenuLayout
from layout import MenuLayout as menuLayout

containers = []
ports = [Port("5000", "5000"), Port("5001", "5001")]
containers.append(Container("Raven"))
containers.append(Container("redis"))
containers.append(Container("mongoDb"))

sg.theme('DarkTanBlue')

menu = [
    [sg.Input(visible=False, key='-hiden-input-')],
    [
        sg.Text('Selected container:', key='-curr-container-', auto_size_text=True, pad=((0, 0), (0, 0)))
    ],
    menuLayout.createContainersRow(containers),
    menuLayout.createElementsRow(),
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createImageSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-image-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0, ))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createBuildSection(), vertical_alignment='c')]],
                     vertical_alignment='c', key='-build-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0, ))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createPortsSection(11), vertical_alignment='c')]],
                     vertical_alignment='c', key='-ports-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createEnvSection(11), vertical_alignment='c')]],
                     vertical_alignment='c', key='-env-section-', visible=False,
                     pad=((0, 0), (0, 0)), title='', border_width=0))],
    [sg.pin(sg.Frame(layout=[[sg.Col(menuLayout.createDependsSection(11), vertical_alignment='c', )]],
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

        sg.Col(menu, pad=((20, 0), (50, 0)), expand_y=True, expand_x=True),
        sg.VSeparator(),
        sg.Column(intput, pad=((20, 0), (150, 10)))
    ]
]

window = sg.Window('Docker-Compose Generator', app_layout, size=(1200, 800), resizable=True,
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
currnetContainer = None
while True:
    event, values = window.read()
    window['-input-'].update(Generator.GenerateYaml(containers))
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if Layout.is_set_container(containers, event):
        # Set currnet container
        currnetContainer = Layout.set_current_container(containers, event, window)
        # set boot options
        Layout.handle_start_visibility_of_all_section(window, currnetContainer)
        Layout.clear_all_inputs(window)
        window.refresh()

    # Handle sections
    Layout.handle_all_section(event, values, window, currnetContainer, containers)
    # Generate yaml
    window['-input-'].update(Generator.GenerateYaml(containers))
    # Visibility
    Layout.handle_all_button_visibility(window,currnetContainer)

window.close()
