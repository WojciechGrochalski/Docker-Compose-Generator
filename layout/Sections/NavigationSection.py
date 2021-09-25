import PySimpleGUI as sg


def create_navigation_section():
    return [
        [
            sg.pin(sg.Text("Choose elements:", font='16', pad=((0, 0), (10, 0)), key="-controls-label-")),
            sg.pin(sg.Button('Name', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-name-")),
            sg.pin(sg.Button('Image', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-image-")),
            sg.pin(sg.Button('Build', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-build-")),
            sg.pin(sg.Button('Ports', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-ports-")),
            sg.pin(sg.Button('Environments', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-env-")),
            sg.pin(sg.Button('Depends', font='16', pad=((10, 0), (10, 0)), enable_events=True, key="-depends-"))
        ],
        [
            sg.pin(sg.Button('Volumes', font='16', pad=((138, 0), (10, 0)), enable_events=True, key="-volumes-"))
        ]
    ]
