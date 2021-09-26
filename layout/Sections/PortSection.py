import PySimpleGUI as sg

from models.Ports import Port

scope = 0


def createPortsSection(count=8):
    global scope
    scope = count
    array = []
    array.extend(addAnotherSectionOfPorts(count))
    return array


def addAnotherSectionOfPorts(count):
    array = []
    controls = [
        sg.pin(sg.Text('Ports', font='16', pad=((250, 0), (20, 20)), key='-label-ports-'))
    ]
    array.append(controls)

    for i in range(1, count + 1):
        inputs = [
            sg.pin(
                sg.Text("Outer port: ", font='12', pad=((50, 0), (20, 0)), enable_events=True,
                        key=f"-outer-port-label-{i}-")),
            sg.pin(sg.In(size=(12, 1), font='12', pad=((5, 0), (20, 0)), enable_events=True,
                         key=f'-outer-port-value-{i}-')),
            sg.pin(
                sg.Text("Inner port: ", font='12', pad=((10, 0), (20, 0)), enable_events=True,
                        key=f"-inner-port-label-{i}-")),
            sg.pin(sg.In(size=(12, 1), font='12', pad=((5, 0), (20, 0)), enable_events=True,
                         key=f'-inner-port-value-{i}-'))]

        array.append(inputs)
    return array


def save_port_section(values, container):
    ports = []
    for i in range(1, scope + 1):
        port = Port(values[f'-outer-port-value-{i}-'], values[f'-inner-port-value-{i}-'])
        ports.append(port.port)
    container.ports = ports
    container.portsCount = len(ports)


def clear_port_section(window):
    for i in range(1, scope + 1):
        window[f'-outer-port-value-{i}-'].update('')
        window[f'-inner-port-value-{i}-'].update('')
