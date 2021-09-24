import PySimpleGUI as sg

from models.Build import Build


def createBuildSection():
    return [
        [
            sg.pin(sg.Text('Build', font='22',  pad=((280, 0), (40, 0)), key='-label-build-'))
        ],
        [
            sg.pin(sg.Text("Dockerfile name: ", font='12', pad=((50, 0), (20, 0)), key="-build-dockerfile-label-")),
            sg.pin(sg.In(size=(30, 1), font='12', pad=((5, 0), (20, 0)), enable_events=True,
                         key='-docerfile-name-value-'))],
        [
            sg.pin(sg.Text("Context: ", font='12', pad=((50, 0), (10, 0)), key="-build-context-label-")),
            sg.pin(
                sg.In(size=(30, 1), font='12', pad=((55, 0), (10, 0)), enable_events=True, key='-context-name-value-'))
        ],
        [
            sg.pin(sg.Button('Apply', font='14', size=(12, 1), pad=((170, 0), (20, 0)), enable_events=True,
                             key='-save-build-')),
            sg.pin(sg.Button('Reset', font='14', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True,
                             key='-reset-build-'))
        ]
    ]


def save_build_section(values, window, container):
    container.build = Build(values['-docerfile-name-value-'], values['-context-name-value-'])
    if container.image:
        if container.build:
            if sg.popup_yes_no(
                    "\n\nYou can't declare build \nand image in one container.\nDo you want reset \nthis section?\n\n",
                    keep_on_top=True) == 'Yes':
                reset_build_value(window, container)


def reset_build_value(window, container):
    clear_build_section(window)
    container.build = None


def clear_build_section(window):
    window['-context-name-value-'].update('')
    window['-docerfile-name-value-'].update('')
