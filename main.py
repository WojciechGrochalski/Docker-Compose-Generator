import PySimpleGUI as sg

from GeneratorHelper import Generator
from handlers.SectionHandler import SectionHandler
from layout import Layout
from layout.Sections.ContainerSection import handle_containers_visibility
from models.Container import Container

containers = [Container('Container', '-container-0-', True)]
currentContainer = containers[0]
scope = 0
for i in range(1, 24):
    containers.append(Container('Container', f'-container-{i}-', False))

sg.theme('DarkBlack')
sg.theme_background_color('#232733')
sg.theme_text_element_background_color('#232733')
sg.theme_button_color('#B0B0B0')
sg.theme_border_width(0)

window = sg.Window('Docker-Compose Generator', size=(1400, 900), resizable=True,
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT).layout(Layout.create_layout(containers))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if Layout.is_set_container(containers, event):
        # Set current container
        currentContainer = Layout.set_current_container(containers, event, window)
        SectionHandler.clear_all_inputs(window)
        window.refresh()
    window['-input-'].update(Generator.GenerateYaml(containers))
    # Handle sections
    SectionHandler.handle_all_section(event, values, window, currentContainer, containers)
    if event == '-add-container-':
        if scope < 26:
            scope += 1
            containers[scope].active = True
            currentContainer = containers[scope]
            SectionHandler.clear_all_inputs(window)
            handle_containers_visibility(window, scope, containers)
        else:
            sg.popup_ok('You reached the limits of containers')
    # import yaml
    if event == '-import-file-':
        containers = SectionHandler.handle_import_button(window, containers)
    # Generate YAML
    window['-input-'].update(Generator.GenerateYaml(containers))

window.close()
