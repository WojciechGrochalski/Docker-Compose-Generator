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
        sg.pin(sg.Button('Save', size=(12, 1), pad=((10, 0), (20, 20)), enable_events=True, key='-save-env-')),
        sg.pin(sg.Text('Environment', font='16', pad=((100, 0), (20, 20)), key='-label-env-'))
    ]
    array.append(controls)
    for i in range(1, count + 1):
        inputs = [
            sg.pin(sg.Text("Enviroment variable: ", font='8', pad=((80, 0), (20, 0)), key=f'-env-label-{i}-')),
            sg.pin(sg.In(size=(26, 1), pad=((5, 0), (20, 0)), enable_events=True, key=f'-env-value-{i}-'))]
        array.append(inputs)
    return array


def save_env_section(values, container):
    envs = []
    for i in range(1, scope + 1):
        enviroment = Environment(values[f'-env-value-{i}-'])
        envs.append(enviroment.enviroment)
    container.environments = envs


def clear_environment_section(window):
    for i in range(1, scope + 1):
        window[f'-env-value-{i}-'].update('')
