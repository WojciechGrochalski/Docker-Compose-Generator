import PySimpleGUI as sg
from GeneratorHelper import GeneratorHelper
from layout import MenuLayout


def appendButton(elements):
    array = [sg.Text("Containers: ", pad=((3, 0), (0, 0)), key='-container-text-')]
    for container in elements:
        array.append(sg.Button(container.name, enable_events=True, key=f'-{container.name}-'))
    array.append(sg.Button("Add container", enable_events=True, key=f'-add-container-'))
    return array


def toggleVisibilityOfSectionImage(window, state):
    window['-image-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionBuild(window, state):
    window['-build-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionPort(window, state):
    window['-ports-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionEnv(window, state):
    window['-env-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)


def toggleVisibilityOfSectionDepends(window, state):
    window['-depends-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionEnv(window, False)


def toggleVisibilityOfSectionControls(window, state):
    window['-controls-label-'].update(visible=state)
    window['-image-'].update(visible=state)
    window['-build-'].update(visible=state)
    window['-ports-'].update(visible=state)
    window['-env-'].update(visible=state)
    window['-depends-'].update(visible=state)


def get_container_name(container, name):
    print(name)
    container.name = name


def setCurrentContainer(containers, event):
    for container in containers:
        if event == f'-{container.name}-':
            # MenuLayout.show_ports_in_range(container.portsCount, True, window)
            return container
    return None


def handleContainerControls(containers, event):
    for container in containers:
        if event == f'-{container.name}-':
            print('exsist', container.name)
            return True
    return False


def handle_controls_section(event, window, values, currnet_container, containers):
    if event == '-save-image-':
        GeneratorHelper.SetContainerName(currnet_container, containers, values['-image-name-value-'])
    if event == '-image-':
        toggleVisibilityOfSectionImage(window, True)
    if event == '-build-':
        toggleVisibilityOfSectionBuild(window, True)
    if event == '-ports-':
        toggleVisibilityOfSectionPort(window, True)
    if event == '-env-':
        toggleVisibilityOfSectionEnv(window, True)
    if event == '-depends-':
        toggleVisibilityOfSectionDepends(window, True)


def handle_button_visibility(window, container):
    if container.portsCount == 0:
        window['-remove-port-'].update(visible=False)
    else:
        window['-remove-port-'].update(visible=True)
    if container.portsCount >= 8:
        window['-add-port-'].update(visible=False)
    else:
        window['-add-port-'].update(visible=True)


def handle_port_section(event, window, container):
    if event == '-add-port-':
        container.portsCount += 1
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
    if event == '-remove-port-':
        container.portsCount -= 1
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
