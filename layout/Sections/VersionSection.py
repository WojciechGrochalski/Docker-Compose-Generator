import PySimpleGUI as sg

from GeneratorHelper import Generator


def create_version_section():
    return [
        [
            sg.pin(sg.Text('Version of Docker-Compose', font='16', pad=((150, 0), (40, 0)), key='-label-version-'))
        ],
        [
            sg.pin(sg.Text("Version: ", font='14', key='-version-', pad=((90, 0), (20, 0)), )),
            sg.pin(sg.In(size=(25, 1), font='14', pad=((10, 0), (20, 0)), enable_events=True, key='-selected-version-value-')),
        ], [
            sg.pin(sg.Button('Apply', font='14',size=(12, 1), pad=((190, 0), (20, 0)), enable_events=True, key='-save-version-'))
        ]
    ]


def save_version_section(values):
    Generator.version = values['-selected-version-value-']


def clear_version_section(window):
    window['-selected-version-value-'].update('')
