import PySimpleGUI as sg


def create_container_section(containers):
    array = []
    array.extend(add_blank_containers_section(containers))
    return array


def add_blank_containers_section(containers):
    array = []
    containers_section = []
    i = 0
    for container in containers:
        if i == 0:
            containers_section.append(
                sg.pin(sg.Button(container.name, enable_events=True, key=f'-container-{i}-', visible=True)))
        else:
            containers_section.append(
                sg.pin(sg.Button(container.name, enable_events=True, key=f'-container-{i}-', visible=False)))
        i += 1
    array.append(containers_section)
    return array


def handle_containers_visibility(window, scope, containers):
    for i in range(0, scope+1):
        window[f'-container-{i}-'].update(visible=True)
    for i in range(scope+1, len(containers)):
        window[f'-container-{i}-'].update(visible=False)
