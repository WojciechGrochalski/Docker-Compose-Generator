import PySimpleGUI as sg


def appendButton(elements):
    array = [sg.Text("Containers: ", pad=((3, 0), (0, 0)), key='-container-text-')]
    for container in elements:
        array.append(sg.Button(container.name, enable_events=True, key=f'-{container.name}-'))
    array.append(sg.Button("Add container", enable_events=True, key=f'-add-container-'))
    return array


def createContainersRow(containers):
    return appendButton(containers)


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
            sg.pin(sg.Text("Container name: ", key='-image-name-', pad=((0, 0), (40, 0)), visible=False)),
            sg.pin(sg.In(size=(25, 1), pad=((0, 0), (40, 0)), enable_events=True, key='-image-name-value-',
                         visible=False)),
        ], [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((130, 0), (20, 0)), enable_events=True, key='-save-image-',
                             visible=False))
        ]
    ]


def createBuildSection():
    return [
        [
            sg.pin(sg.Text("Dockerfile name: ", pad=((0, 0), (0, 0)), key="-build-dockerfile-label-", visible=False)),
            sg.pin(sg.In(size=(30, 1), pad=((5, 0), (0, 0)), enable_events=True, key='-docerfile-name-value-',
                         visible=False))],
        [
            sg.pin(sg.Text("Context: ", pad=((0, 0), (10, 0)), key="-build-context-label-", visible=False)),
            sg.pin(sg.In(size=(30, 1), pad=((52, 0), (10, 0)), enable_events=True, key='-context-name-value-',
                         visible=False))
        ],
        [
            sg.pin(sg.Button('Save', size=(12, 1), pad=((160, 0), (20, 0)), enable_events=True, key='-save-build-',
                             visible=False))
        ]
    ]


def createEnvSection():
    return [
        [

        ]
    ]


def createPortsSection(count=3):
    array = [addAnotherSectionOfPorts(count), [
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-port-',
                         visible=False)),
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-port-',
                         visible=False))
    ]]
    return array


def addAnotherSectionOfPorts(count):
    array = []
    outerarray = []
    for i in range(count):
        array.append(sg.Frame(
            layout=[[sg.Col([[
                sg.pin(sg.Text("Outer port: ", pad=((0, 0), (0, 0)), key=f"-outer-port-label-{i}-", visible=False)),
                sg.pin(sg.In(size=(10, 1), pad=((5, 0), (0, 0)), enable_events=True, key=f'-outer-port-value-{i}-',
                             visible=False)),
                sg.pin(sg.Text("Inner port: ", pad=((10, 0), (0, 0)), key=f"-inner-port-label-{i}-", visible=False)),
                sg.pin(sg.In(size=(10, 1), pad=((5, 0), (0, 0)), enable_events=True, key=f'-inner-port-value-{i}-',
                             visible=False))]], vertical_alignment='c')]], vertical_alignment='c', title='',
            border_width=0))
    for item in array:
        outerarray.append(item)
    return outerarray


def toggleVisibilityOfSectionImage(window, state):
    window['-image-name-'].update(visible=state)
    window['-image-name-value-'].update(visible=state)
    window['-save-image-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)


def toggleVisibilityOfSectionBuild(window, state):
    window['-build-dockerfile-label-'].update(visible=state)
    window['-docerfile-name-value-'].update(visible=state)
    window['-build-context-label-'].update(visible=state)
    window['-context-name-value-'].update(visible=state)
    window['-save-build-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)


def toggleVisibilityOfSectionPort(window, state, count=3):
    for i in range(count):
        window[f'-outer-port-label-{i}-'].update(visible=state)
        window[f'-outer-port-value-{i}-'].update(visible=state)
        window[f'-inner-port-label-{i}-'].update(visible=state)
        window[f'-inner-port-value-{i}-'].update(visible=state)
    window['-add-port-'].update(visible=state)
    window['-save-port-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)


def toggleVisibilityOfSectionEnv(window, state):
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)


def toggleVisibilityOfSectionControls(window, state):
    window['-controls-label-'].update(visible=state)
    window['-image-'].update(visible=state)
    window['-build-'].update(visible=state)
    window['-ports-'].update(visible=state)
    window['-env-'].update(visible=state)
    window['-depends-'].update(visible=state)


def updateContainerName(container, name):
    print(name)
    container.name = name


def setCurrentContainer(containers, event):
    for container in containers:
        if event == f'-{container.name}-':
            print(container.name)
            return container
    return None


def handleContainerControls(containers, event):
    for container in containers:
        if event == f'-{container.name}-':
            print(container.name)
            return True
    return False
