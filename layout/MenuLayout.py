import PySimpleGUI as sg
from layout import Layout
from models.Depends import Dependency
from models.Environment import Environment
from models.Ports import Port


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
    controls = [
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-port-')),
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-add-port-')),
        sg.pin(sg.Button('Remove', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-remove-port-')),
    ]
    array.append(controls)

    for i in range(1, count):
        inputs = [
            sg.pin(sg.Text("Outer port: ", pad=((0, 0), (40, 0)), enable_events=True, key=f"-outer-port-label-{i}-")),
            sg.pin(sg.In(size=(10, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-outer-port-value-{i}-')),
            sg.pin(sg.Text("Inner port: ", pad=((10, 0), (40, 0)), enable_events=True, key=f"-inner-port-label-{i}-")),
            sg.pin(sg.In(size=(10, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-inner-port-value-{i}-'))]

        array.append(inputs)
    return array


def toggle_ports_in_range(scope, state, window):
    if scope == 0:
        for i in range(1, 11):
            window[f'-outer-port-label-{i}-'].update(visible=False)
            window[f'-outer-port-value-{i}-'].update(visible=False)
            window[f'-inner-port-label-{i}-'].update(visible=False)
            window[f'-inner-port-value-{i}-'].update(visible=False)
    else:
        for i in range(1, scope+1):
            window[f'-outer-port-label-{i}-'].update(visible=state)
            window[f'-outer-port-value-{i}-'].update(visible=state)
            window[f'-inner-port-label-{i}-'].update(visible=state)
            window[f'-inner-port-value-{i}-'].update(visible=state)
        for i in range(scope + 1, 11):
            window[f'-outer-port-label-{i}-'].update(visible=False)
            window[f'-outer-port-value-{i}-'].update(visible=False)
            window[f'-inner-port-label-{i}-'].update(visible=False)
            window[f'-inner-port-value-{i}-'].update(visible=False)


def save_port_section(values, container):
    ports = []
    for i in range(1, container.portsCount + 1):
        port = Port(values[f'-outer-port-value-{i}-'], values[f'-inner-port-value-{i}-'])
        ports.append(port.port)
    container.ports = ports


def createEnvSection(count=1):
    array = []
    array.extend(addAnotherSectionOfEnv(count))
    return array


def addAnotherSectionOfEnv(count):
    array = []
    controls = [
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-env-')),
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-env-')),
        sg.pin(sg.Button('Remove', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-remove-env-')),
    ]
    array.append(controls)
    for i in range(1, count):
        inputs = [
            sg.pin(sg.Text("Enviroment variable: ", pad=((0, 0), (40, 0)), key=f'-env-label-{i}-')),
            sg.pin(sg.In(size=(26, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-env-value-{i}-'))]
        array.append(inputs)
    return array


def toggle_env_in_range(scope, state, window):
    if scope == 0:
        for i in range(1, 11):
            window[f'-env-label-{i}-'].update(visible=False)
            window[f'-env-value-{i}-'].update(visible=False)
    else:
        for i in range(1, scope+1):
            window[f'-env-label-{i}-'].update(visible=state)
            window[f'-env-value-{i}-'].update(visible=state)
        for i in range(scope + 1, 11):
            window[f'-env-label-{i}-'].update(visible=False)
            window[f'-env-value-{i}-'].update(visible=False)


def save_env_section(values, container):
    envs = []
    for i in range(1, container.environmentsCount + 1):
        enviroment = Environment(values[f'-env-value-{i}-'])
        envs.append(enviroment.enviroment)
    container.environments = envs


def createDependsSection(count=1):
    array = []
    array.extend(addAnotherSectionOfDepends(count))
    return array


def addAnotherSectionOfDepends(count):
    array = []
    controls = [
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-save-depends-')),
        sg.pin(sg.Button('Add another', size=(12, 1), pad=((70, 0), (20, 0)), enable_events=True, key='-add-depends-')),
        sg.pin(sg.Button('Remove', size=(12, 1), pad=((10, 0), (20, 0)), enable_events=True, key='-remove-depends-')),
    ]
    array.append(controls)
    for i in range(1, count):
        inputs = [
            sg.pin(sg.Text("Depends on: ", pad=((0, 0), (40, 0)), key=f"-depends-label-{i}-")),
            sg.pin(sg.In(size=(26, 1), pad=((5, 0), (40, 0)), enable_events=True, key=f'-depends-value-{i}-'))]
        array.append(inputs)
    return array


def toggle_depends_in_range(scope, state, window):
    if scope == 0:
        for i in range(1, 11):
            window[f'-depends-label-{i}-'].update(visible=False)
            window[f'-depends-value-{i}-'].update(visible=False)
    else:
        for i in range(1, scope+1):
            window[f'-depends-label-{i}-'].update(visible=state)
            window[f'-depends-value-{i}-'].update(visible=state)
        for i in range(scope + 1, 11):
            window[f'-depends-label-{i}-'].update(visible=False)
            window[f'-depends-value-{i}-'].update(visible=False)


def save_depends_section(values, container):
    depends = []
    for i in range(1, container.dependsCount + 1):
        depend = Dependency(values[f'-depends-value-{i}-'])
        depends.append(depend.depend)
    container.depends = depends
