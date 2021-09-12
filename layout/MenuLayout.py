import PySimpleGUI as sg
from layout import Layout


def createContainersRow(containers):
    return Layout.appendButton(containers)


def createElementsRow():
    return [
        sg.pin(sg.Text("Choose elements:", pad=((0, 0), (10, 0)), key="-controls-label-", visible=False)),
        sg.pin(sg.Button('Image', pad=((5, 0), (10, 0)), enable_events=True, key="-image-", visible=False)),
        sg.pin(sg.Button('Build', pad=((10, 0), (10, 0)), enable_events=True, key="-build-", visible=False)),
        sg.pin(sg.Button('Ports', pad=((10, 0), (10, 0)), enable_events=True, key="-ports-", visible=False)),
        sg.pin(sg.Button('Enviroments', pad=((10, 0), (10, 0)), enable_events=True, key="-env-", visible=False)),
        sg.pin(sg.Button('Depends', pad=((10, 0), (10, 0)), enable_events=True, key="-depends-", visible=False))]


def createImageSection():
    return [
        [
            sg.pin(sg.Text("Container name: ", key='-image-name-', pad=((0, 0), (40, 0)), )),
            sg.pin(sg.In(size=(25, 1), pad=((5, 0), (40, 0)), enable_events=True, key='-image-name-value-')),
        ], [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((130, 0), (20, 0)), enable_events=True, key='-save-image-'))
        ]
    ]


def createBuildSection():
    return [
        [
            sg.pin(sg.Text("Dockerfile name: ", pad=((0, 0), (40, 0)), key="-build-dockerfile-label-")),
            sg.pin(sg.In(size=(30, 1), pad=((5, 0), (40, 0)), enable_events=True, key='-docerfile-name-value-'))],
        [
            sg.pin(sg.Text("Context: ", pad=((0, 0), (10, 0)), key="-build-context-label-")),
            sg.pin(sg.In(size=(30, 1), pad=((52, 0), (10, 0)), enable_events=True, key='-context-name-value-'))
        ],
        [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((160, 0), (20, 0)), enable_events=True, key='-save-build-'))
        ]
    ]


def createPortsSection(count=1):
    array = []
    array.extend(addAnotherSectionOfPorts(count))
    return array


def addAnotherSectionOfPorts(count):
    array = []
    for i in range(count):
        inputs = [
            sg.pin(sg.Text("Outer port: ", pad=((0, 0), (40, 0)), key=f"-outer-port-label-{i}-")),
            sg.pin(sg.In(size=(10, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-outer-port-value-{i}-')),
            sg.pin(sg.Text("Inner port: ", pad=((10, 0), (40, 0)), key=f"-inner-port-label-{i}-")),
            sg.pin(sg.In(size=(10, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-inner-port-value-{i}-'))]
        array.append(inputs)

    controls = [
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-port-')),
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-port-'))
    ]

    array.append(controls)
    return array


def createEnvSection(count=1):
    array = []
    array.extend(addAnotherSectionOfEnv(count))
    return array


def addAnotherSectionOfEnv(count):
    array = []
    for i in range(count):
        inputs = [
            sg.pin(sg.Text("Enviroment variable: ", pad=((0, 0), (40, 0)), key=f"-env-label-{i}-")),
            sg.pin(sg.In(size=(26, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-env-value-{i}-'))]
        array.append(inputs)

    controls = [
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-env-')),
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-env-'))
    ]
    array.append(controls)
    return array


def createDependsSection(count=1):
    array = []
    array.extend(addAnotherSectionOfDepends(count))
    return array


def addAnotherSectionOfDepends(count):
    array = []
    for i in range(count):
        inputs = [
            sg.pin(sg.Text("Depends on: ", pad=((0, 0), (40, 0)), key=f"-depends-label-{i}-")),
            sg.pin(sg.In(size=(26, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-depends-value-{i}-'))]
        array.append(inputs)

    controls = [
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-depends-')),
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-depends-'))
    ]
    array.append(controls)
    return array
