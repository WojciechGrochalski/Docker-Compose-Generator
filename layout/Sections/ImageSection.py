import PySimpleGUI as sg


def createImageSection():
    return [
        [
            sg.pin(sg.Text('Image', font='16', pad=((210, 0), (40, 0)), key='-label-image-'))
        ],
        [
            sg.pin(sg.Text("Container image: ",font='8', key='-image-name-', pad=((50, 0), (20, 0)), )),
            sg.pin(sg.In(size=(25, 1), pad=((5, 0), (20, 0)), enable_events=True, key='-image-name-value-')),
        ], [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((180, 0), (20, 0)), enable_events=True, key='-save-image-'))
        ]
    ]
