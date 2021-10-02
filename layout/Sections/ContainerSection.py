import PySimpleGUI as sg


def create_container_section(containers):
    return add_blank_containers_section(containers)


def add_blank_containers_section(containers):
    array = []
    containers_section_1 = []
    containers_section_2 = []
    containers_section_3 = []
    i = 0
    for container in containers:
        if i == 0:
            containers_section_1.append(
                sg.pin(sg.Button(container.name, font='19', enable_events=True, key=f'-container-{i}-',
                                 pad=((8, 0), (10, 0)), visible=True)))
        else:
            if i <= 10:
                containers_section_1.append(
                    sg.pin(sg.Button(container.name, font='19', enable_events=True, key=f'-container-{i}-',
                                     pad=((8, 0), (10, 0)),
                                     visible=False)))
            if 10 < i <= 20:
                containers_section_2.append(
                    sg.pin(sg.Button(container.name, font='19', enable_events=True, key=f'-container-{i}-',
                                     pad=((8, 0), (10, 0)),
                                     visible=False)))
            if 20 < i < 30:
                containers_section_3.append(
                    sg.pin(sg.Button(container.name, font='19', enable_events=True, key=f'-container-{i}-',
                                     pad=((8, 0), (10, 0)),
                                     visible=False)))
        i += 1
    array.append(containers_section_1)
    array.append(containers_section_2)
    array.append(containers_section_3)
    return array


def handle_containers_visibility(window, containers):
    for container in containers:
        if container.active:
            window[container.key].update(visible=True)
        else:
            window[container.key].update(visible=False)
