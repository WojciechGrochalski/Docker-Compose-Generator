import PySimpleGUI as sg


def create_name_section():
    return [
        [
            sg.pin(sg.Text('Name', font='16', pad=((210, 0), (40, 0)), key='-label-name-'))
        ],
        [
            sg.pin(sg.Text("Container name: ", font='8', key='-container-name-', pad=((50, 0), (20, 0)), )),
            sg.pin(sg.In(size=(25, 1), pad=((5, 0), (20, 0)), enable_events=True, key='-container-name-value-')),
        ], [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((180, 0), (20, 0)), enable_events=True, key='-save-name-'))
        ]
    ]


def save_container_name_section(values, window, container):
    name = values['-container-name-value-']
    window[container.key].update(name)
    container.name = values['-container-name-value-']
