import PySimpleGUI as sg

from models.Depends import Dependency

scope = 0


def createDependsSection(count=7):
    global scope
    scope = count
    array = []
    array.extend(addAnotherSectionOfDepends(count))
    return array


def addAnotherSectionOfDepends(count):
    array = []
    controls = [
        sg.pin(sg.Text('Dependency', font='16', pad=((230, 0), (20, 20)), key='-label-dependency-'))
    ]
    array.append(controls)
    for i in range(1, count + 1):
        inputs = [
            sg.pin(sg.Text("Depends on: ", font='12', pad=((50, 0), (20, 0)), key=f"-depends-label-{i}-")),
            sg.pin(
                sg.In(size=(26, 1), font='12', pad=((5, 0), (20, 0)), enable_events=True, key=f'-depends-value-{i}-'))]
        array.append(inputs)
    return array


def save_depends_section(values, container):
    depends = []
    for i in range(1, scope + 1):
        depend = Dependency(values[f'-depends-value-{i}-'])
        depends.append(depend.dependency)
    container.depends = depends
    container.dependsCount = len(depends)


def clear_dependency_section(window):
    for i in range(1, scope + 1):
        window[f'-depends-value-{i}-'].update('')
