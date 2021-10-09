import PySimpleGUI as sg

from models.Environment import Environment

scope = 0


def createEnvSection(count=8):
    global scope
    scope = count
    array = []
    array.extend(addAnotherSectionOfEnv(count))
    return array


def addAnotherSectionOfEnv(count):
    array = []
    controls = [
        sg.pin(sg.Text('Environment', font='16', pad=((200, 0), (20, 10)), key='-label-env-'))
    ]
    array.append(controls)
    for i in range(1, count + 1):
        inputs = [
            sg.pin(sg.Text("Enviroment variable: ", font='12', pad=((20, 0), (20, 0)), key=f'-env-label-{i}-')),
            sg.pin(sg.In(size=(28, 1), font='12', pad=((5, 20), (20, 0)), enable_events=True, key=f'-env-value-{i}-'))]
        array.append(inputs)
    apply = [
        sg.pin(sg.Button('Apply', font='14', size=(12, 1), pad=((197, 0), (20, 0)), enable_events=True,
                         key='-save-envs-'))
    ]
    array.append(apply)
    return array


def save_env_section(values, container):
    envs = []
    for i in range(1, scope + 1):
        environment = Environment(values[f'-env-value-{i}-'])
        envs.append(environment.environment)
    container.environments = envs
    container.environmentsCount = len(envs)


def clear_environment_section(window):
    for i in range(1, scope + 1):
        window[f'-env-value-{i}-'].update('')
