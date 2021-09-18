import PySimpleGUI as sg
from GeneratorHelper import Generator
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


def toggle_visibilit_of_section_controls(window, state):
    window['-controls-label-'].update(visible=state)
    window['-image-'].update(visible=state)
    window['-build-'].update(visible=state)
    window['-ports-'].update(visible=state)
    window['-env-'].update(visible=state)
    window['-depends-'].update(visible=state)


def get_container_name(container, name):
    print(name)
    container.name = name


def set_current_container(containers, event, window):
    for container in containers:
        if event == f'-{container.name}-':
            window['-curr-container-'].update(f'Selected container: {container.name}')
            return container
    return None


def is_set_container(containers, event):
    for container in containers:
        if event == f'-{container.name}-':
            return True
    return False


def handle_controls_section(event, values, window, currnet_container, containers):
    if event == '-save-image-':
        Generator.SetContainerName(currnet_container, containers, values['-image-name-value-'])
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


def handle_all_section(event, values, window, container, containers):
    # Controls
    handle_controls_section(event, values, window, container, containers)
    # Ports
    handle_port_section(event, values, window, container)
    # Environment
    handle_env_section(event, values, window, container)
    # Dependency
    handle_depends_section(event, values, window, container)


def toggle_all_section(window, container):
    # Ports
    MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
    # Enviroments
    MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
    # Dependency
    MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)


def handle_start_visibility_of_all_section(window, container):
    # Controls
    toggle_visibilit_of_section_controls(window, True)
    # Ports
    MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
    # Enviroments
    MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
    # Dependency
    MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)


def handle_all_button_visibility(window, container):
    # Ports
    handle_ports_button_visibility(window, container)
    # Enviroments
    handle_env_button_visibility(window, container)
    # Dependency
    handle_dependency_button_visibility(window, container)


def handle_ports_button_visibility(window, container, max_range=8):
    if container.portsCount == 0:
        window['-remove-port-'].update(visible=False)
    else:
        window['-remove-port-'].update(visible=True)
    if container.portsCount > max_range:
        window['-add-port-'].update(visible=False)
    else:
        window['-add-port-'].update(visible=True)


def handle_env_button_visibility(window, container, max_range=8):
    if container.environmentsCount == 0:
        window['-remove-env-'].update(visible=False)
    else:
        window['-remove-env-'].update(visible=True)
    if container.environmentsCount > max_range:
        window['-add-env-'].update(visible=False)
    else:
        window['-add-env-'].update(visible=True)


def handle_dependency_button_visibility(window, container, max_range=8):
    if container.dependsCount == 0:
        window['-remove-depends-'].update(visible=False)
    else:
        window['-remove-depends-'].update(visible=True)
    if container.dependsCount > max_range:
        window['-add-depends-'].update(visible=False)
    else:
        window['-add-depends-'].update(visible=True)


def handle_env_section(event, values, window, container):
    if event == '-add-env-':
        container.environmentsCount += 1
        MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
    if event == '-remove-env-':
        container.environmentsCount -= 1
        MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
    if event == '-save-env-':
        MenuLayout.save_env_section(values, container)


def handle_port_section(event, values, window, container):
    if event == '-add-port-':
        container.portsCount += 1
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
    if event == '-remove-port-':
        container.portsCount -= 1
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
    if event == '-save-port-':
        MenuLayout.save_port_section(values, container)


def handle_depends_section(event, values, window, container):
    if event == '-add-depends-':
        container.dependsCount += 1
        MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)
    if event == '-remove-depends-':
        container.dependsCount -= 1
        MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)
    if event == '-save-depends-':
        MenuLayout.save_depends_section(values, container)


def clear_all_inputs(window):
    for i in range(1, 11):
        window[f'-env-value-{i}-'].update('')
        window[f'-depends-value-{i}-'].update('')
        window[f'-outer-port-value-{i}-'].update('')
        window[f'-inner-port-value-{i}-'].update('')
