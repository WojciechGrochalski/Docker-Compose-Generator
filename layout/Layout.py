import PySimpleGUI as sg

from GeneratorHelper import Generator
from layout.Sections.BuildSection import createBuildSection
from layout.Sections.ContainerSection import create_container_section
from layout.Sections.DependencySection import createDependsSection
from layout.Sections.EnvironmentSection import createEnvSection
from layout.Sections.ImageSection import createImageSection
from layout.Sections.NameSection import create_name_section
from layout.Sections.NavigationSection import create_navigation_section
from layout.Sections.PortSection import createPortsSection
from layout.Sections.VersionSection import create_version_section
from layout.Sections.VolumesSection import create_volume_section


def toggleVisibilityOfSectionName(window, state):
    window['-container-name-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionImage(window, state):
    window['-image-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionBuild(window, state):
    window['-build-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionPort(window, state):
    window['-ports-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionEnv(window, state):
    window['-env-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionDepends(window, state):
    window['-depends-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionVersion(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def toggleVisibilityOfSectionVolumes(window, state):
    window['-volumes-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVersion(window, False)


def toggleVisibilityOfSectionVersion(window, state):
    window['-version-section-'].update(visible=state)
    if state:
        toggleVisibilityOfSectionName(window, False)
        toggleVisibilityOfSectionImage(window, False)
        toggleVisibilityOfSectionBuild(window, False)
        toggleVisibilityOfSectionPort(window, False)
        toggleVisibilityOfSectionEnv(window, False)
        toggleVisibilityOfSectionDepends(window, False)
        toggleVisibilityOfSectionVolumes(window, False)


def set_current_container(containers, event, window):
    for container in containers:
        if event == container.key:
            window['-curr-container-'].update(f'Selected container: {container.name}')
            return container
    return None


def update_gui(window, container):
    # Name
    window['-container-name-value-'].update(container.name)
    # Image
    window['-image-name-value-'].update(container.image)
    # Build
    if container.build is not None:
        window['-context-name-value-'].update(container.build.context)
        window['-docerfile-name-value-'].update(container.build.dockerfile)
    # Ports
    ports = container.ports
    for i in range(0, container.portsCount):
        if len(ports[i]) > 0:
            port = ports[i].split()[1]
            port = port.replace('"', '')
            window[f'-outer-port-value-{i + 1}-'].update(port.split(':')[0])
            window[f'-inner-port-value-{i + 1}-'].update(port.split(':')[1])
    # Environments
    envs = container.environments
    for i in range(0, container.environmentsCount):
        if len(envs[i]) > 0:
            env = envs[i].split()[1]
            window[f'-env-value-{i + 1}-'].update(env)
    # Dependency
    dependency = container.dependency
    for i in range(0, container.dependsCount):
        if len(dependency[i]) > 0:
            depend = dependency[i].split()[1]
            window[f'-depends-value-{i + 1}-'].update(depend)
    # Volumes
    volumes = container.volumes
    for i in range(0, container.volumesCount):
        if len(volumes[i]) > 0:
            volume = volumes[i].split()[1]
            window[f'-volume-value-{i + 1}-'].update(volume)


def is_set_container(containers, event):
    for container in containers:
        if event == container.key:
            return True
    return False


def create_layout(containers):
    menu = [
        [
            sg.Text('Selected container: Container', font='24', key='-curr-container-', auto_size_text=True,
                    pad=((5, 0), (0, 0)))
        ],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_navigation_section(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-navigation-section-',
                         background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_name_section(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-container-name-section-', visible=False,
                         background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createImageSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-image-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createBuildSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-build-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createPortsSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-ports-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createEnvSection(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-env-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(createDependsSection(), vertical_alignment='c', )]],
                         vertical_alignment='c', key='-depends-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_volume_section(), vertical_alignment='c', )]],
                         vertical_alignment='c', key='-volumes-section-', visible=False, background_color='#232733',
                         pad=((0, 0), (0, 0)), title='', border_width=0))],
        [sg.pin(sg.Frame(layout=[[sg.Col(create_version_section(), vertical_alignment='c')]],
                         vertical_alignment='c', key='-version-section-',
                         background_color='#232733', visible=False,
                         pad=((0, 0), (0, 0)), title='', border_width=0))]
    ]

    docker_compose_text = [
        [
            sg.Button('Import Docker-Compose', font='16', pad=((10, 0), (10, 10)), enable_events=True,
                      key='-import-file-'),
            sg.Button('Export Docker-Compose', font='16', pad=((10, 0), (10, 10)), enable_events=True,
                      key='-export-file-')
        ],
        [
            sg.Multiline(Generator.GenerateYaml(containers), font='15', autoscroll=True, auto_size_text=True,
                         expand_x=True,
                         background_color='#1E1E1E',
                         size=(200, 200), key="-input-")
        ]
    ]

    containers = [
        [sg.Input(visible=False, key='-hidden-input-')],
        [
            sg.pin(sg.Frame(layout=[[sg.Col(create_container_section(containers), vertical_alignment='c')]],
                            vertical_alignment='c', key='-containers-section-', background_color='#232733',
                            pad=((0, 0), (20, 30)), title='', border_width=0))
        ],
        [
            sg.Button("Add container", font='16', enable_events=True, key='-add-container-', pad=((10, 0), (0, 10))),
            sg.Button("Remove container", font='16', enable_events=True, key='-remove-container-',
                      pad=((10, 0), (0, 10))),
            sg.Button("Select version", font='16', enable_events=True, key='-select-version-', pad=((10, 0), (0, 10))),
        ],
        sg.HSeparator()
    ]

    return [
        [
            containers,
            sg.Col(menu, pad=((20, 0), (20, 0)), expand_y=True),
            sg.VSeparator(),
            sg.Column(docker_compose_text, pad=((20, 0), (20, 10)), expand_x=True, expand_y=True)
        ]
    ]
