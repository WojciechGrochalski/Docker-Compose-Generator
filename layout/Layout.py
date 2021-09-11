import PySimpleGUI as sg


def appendButton(elements):
    array = [sg.Text("Containers: ",pad=((3, 0), (0, 0)), key='-container-text-')]
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
        sg.pin(sg.Button('Enviroments', pad=((10, 0), (10, 0)), enable_events=True, key="-env-", visible=False)),
        sg.pin(sg.Button('Depends', pad=((10, 0), (10, 0)), enable_events=True, key="-depends-", visible=False))]


def createImageSection():
    return [
        sg.Text("Container name: ", key='-image-name-', pad=((10, 0), (20, 0)), visible=False),
        sg.In(size=(25, 1), enable_events=True, key='-image-name-value-', visible=False),
        sg.Button('Ok', enable_events=True, key='-save-image-name-', visible=False)
    ]


def toggleVisibilityOfSectionImage(window, state):
    window['-image-name-'].update(visible=state)
    window['-image-name-value-'].update(visible=state)
    window['-save-image-name-'].update(visible=state)


def toggleVisibilityOfSectionControls(window, state):
    window['-controls-label-'].update(visible=state)
    window['-image-'].update(visible=state)
    window['-build-'].update(visible=state)
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
