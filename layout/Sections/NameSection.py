import PySimpleGUI as sg


def create_name_section():
    return [
        [
            sg.pin(sg.Text('Name', font='22', pad=((230, 0), (40, 0)), key='-label-name-'))
        ],
        [
            sg.pin(sg.Text("Container name: ", font='12', key='-container-name-', pad=((20, 0), (20, 0)), )),
            sg.pin(sg.In(size=(25, 1), font='12', pad=((5, 20), (20, 0)),
                         key='-container-name-value-')),
        ], [
            sg.pin(sg.Button('Apply', font='14', size=(12, 1), pad=((190, 0), (20, 0)), enable_events=True,
                             key='-save-name-'))
        ]
    ]


def save_container_name_section(values, window, container):
    name = values['-container-name-value-']
    window[container.key].update(name)
    window['-curr-container-'].update(f'Selected container: {name}')
    container.name = values['-container-name-value-']


def clear_name_section(window):
    window['-container-name-value-'].update('')
