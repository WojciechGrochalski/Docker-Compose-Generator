import PySimpleGUI as sg


def createImageSection():
    return [
        [
            sg.pin(sg.Text('Image', font='22', pad=((260, 0), (40, 0)), key='-label-image-'))
        ],
        [
            sg.pin(sg.Text("Container image: ", font='12', key='-image-name-', pad=((50, 0), (20, 0)), )),
            sg.pin(sg.In(size=(25, 1), font='12', pad=((5, 0), (20, 0)), enable_events=True, key='-image-name-value-')),
        ], [
            sg.pin(sg.Button('Apply', font='14', size=(12, 1), pad=((170, 0), (20, 0)), enable_events=True, key='-save-image-')),
            sg.pin(sg.Button('Reset', font='14', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-reset-image-'))
        ]
    ]


def save_container_image_section(values, window, container):
    container.image = values['-image-name-value-']
    if container.build:
        if sg.popup_yes_no("\n\nYou can't declare build \nand image in one container.\nDo you want reset \nthis section?\n\n",
                           keep_on_top=True) == 'Yes':
            reset_image_value(window, container)


def reset_image_value(window, container):
    clear_image_section(window)
    container.image = None


def clear_image_section(window):
    window['-image-name-value-'].update('')
