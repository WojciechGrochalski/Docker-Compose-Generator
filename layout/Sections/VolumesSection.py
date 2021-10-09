import PySimpleGUI as sg

from models.Volume import Volume

scope = 0


def create_volume_section(count=8):
    global scope
    scope = count
    array = []
    array.extend(add_another_section_of_volume(count))
    return array


def add_another_section_of_volume(count):
    array = []
    controls = [
        sg.pin(sg.Text('Volumes', font='16', pad=((225, 0), (20, 10)), key='-label-volume-'))
    ]
    array.append(controls)
    for i in range(1, count + 1):
        inputs = [
            sg.pin(sg.Text("Volume: ", font='12', pad=((30, 0), (20, 0)), key=f'-volume-label-{i}-')),
            sg.pin(
                sg.In(size=(35, 1), font='12', pad=((5, 20), (20, 0)), enable_events=True, key=f'-volume-value-{i}-'))]
        array.append(inputs)
    apply = [
        sg.pin(sg.Button('Apply', font='14', size=(12, 1), pad=((190, 0), (20, 0)), enable_events=True,
                         key='-save-volumes-'))
    ]
    array.append(apply)
    return array


def save_volume_section(values, container):
    volumes = []
    for i in range(1, scope + 1):
        volume = Volume(values[f'-volume-value-{i}-'])
        volumes.append(volume.volume)
    container.volumes = volumes
    container.volumesCount = len(volumes)


def clear_volume_section(window):
    for i in range(1, scope + 1):
        window[f'-volume-value-{i}-'].update('')
