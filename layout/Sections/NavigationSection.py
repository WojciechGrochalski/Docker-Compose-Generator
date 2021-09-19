import PySimpleGUI as sg


def create_navigation_section():
    return [
        [
            sg.pin(sg.Text("Choose elements:", font='10', pad=((0, 0), (10, 0)), key="-controls-label-")),
            sg.pin(sg.Button('Name', pad=((10, 0), (10, 0)), enable_events=True, key="-name-")),
            sg.pin(sg.Button('Image', pad=((10, 0), (10, 0)), enable_events=True, key="-image-")),
            sg.pin(sg.Button('Build', pad=((10, 0), (10, 0)), enable_events=True, key="-build-")),
            sg.pin(sg.Button('Ports', pad=((10, 0), (10, 0)), enable_events=True, key="-ports-")),
            sg.pin(sg.Button('Enviroments', pad=((10, 0), (10, 0)), enable_events=True, key="-env-")),
            sg.pin(sg.Button('Depends', pad=((10, 0), (10, 0)), enable_events=True, key="-depends-"))
        ]
    ]
