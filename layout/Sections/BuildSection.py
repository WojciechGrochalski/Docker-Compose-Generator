import PySimpleGUI as sg


def createBuildSection():
    return [
        [
            sg.pin(sg.Text('Build', font='16', pad=((210, 0), (40, 0)), key='-label-build-'))
        ],
        [

            sg.pin(sg.Text("Dockerfile name: ", font='8', pad=((50, 0), (20, 0)), key="-build-dockerfile-label-")),
            sg.pin(sg.In(size=(30, 1), pad=((5, 0), (20, 0)), enable_events=True, key='-docerfile-name-value-'))],
        [
            sg.pin(sg.Text("Context: ", font='8', pad=((50, 0), (10, 0)), key="-build-context-label-")),
            sg.pin(sg.In(size=(30, 1), pad=((65, 0), (10, 0)), enable_events=True, key='-context-name-value-'))
        ],
        [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((170, 0), (20, 0)), enable_events=True, key='-save-build-'))
        ]
    ]
