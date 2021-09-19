import PySimpleGUI as sg

from layout.Sections.BuildSection import createBuildSection
from layout.Sections.ContainerSection import create_container_section
from layout.Sections.DependencySection import createDependsSection
from layout.Sections.EnvironmentSection import createEnvSection
from layout.Sections.ImageSection import createImageSection
from layout.Sections.NameSection import create_name_section
from layout.Sections.NavigationSection import create_navigation_section
from layout.Sections.PortSection import createPortsSection


def toggleVisibilityOfSectionName(window, state):
    window['-container-name-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionImage(window, state):
    window['-image-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionBuild(window, state):
    window['-build-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionPort(window, state):
    window['-ports-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionEnv(window, state):
    window['-env-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionDepends(window, state):
    window['-depends-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionEnv(window, False)


def toggle_visibilit_of_section_controls(window, state):
    window['-controls-label-'].update(visible=state)
    window['-name-'].update(visible=state)
    window['-image-'].update(visible=state)
    window['-build-'].update(visible=state)
    window['-ports-'].update(visible=state)
    window['-env-'].update(visible=state)
    window['-depends-'].update(visible=state)


def set_current_container(containers, event, window):
    for container in containers:
        if event == container.key:
            window['-curr-container-'].update(f'Selected container: {container.name}')
            return container
    return None


def is_set_container(containers, event):
    for container in containers:
        if event == container.key:
            return True
    return False


def create_layout(containers):
    menu = [
        [
            sg.Text('Selected container:', key='-curr-container-', auto_size_text=True, pad=((0, 0), (0, 0)))
        ],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_navigation_section(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-navigation-section-',
                         background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_name_section(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-container-name-section-', visible=False,
                         background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createImageSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-image-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createBuildSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-build-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createPortsSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-ports-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createEnvSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-env-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createDependsSection(2), vertical_alignment='c', )]],
                         vertical_alignment='c', key='-depends-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
    ]

    intput = [
        [
            sg.Text(auto_size_text=True, background_color='#1E1E1E', size=(100, 200), key="-input-")
        ]
    ]

    containers = [
        [sg.Input(visible=False, key='-hiden-input-')],
        [
            sg.pin(sg.Frame(layout=[[sg.Col(create_container_section(containers), vertical_alignment='c')]],
                            vertical_alignment='c', key='-containers-section-', background_color='#232733',
                            pad=((0, 0), (20, 30)), title='', border_width=0))
        ],
        [
            sg.Button("Add container", enable_events=True, key=f'-add-container-', pad=((10, 0), (0, 10))),
        ],
        sg.HSeparator()
    ]

    return [
        [
            containers,
            sg.Col(menu, pad=((20, 0), (50, 0)), expand_y=True, expand_x=True),
            sg.VSeparator(),
            sg.Column(intput, pad=((20, 0), (20, 10)))
        ]
    ]
