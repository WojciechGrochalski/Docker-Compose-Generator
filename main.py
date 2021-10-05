import PySimpleGUI as sg

from GeneratorHelper import Generator
from handlers.SectionHandler import SectionHandler
from layout import Layout
from layout.Sections.ContainerSection import handle_containers_visibility
from models.Container import Container

containers = [Container('New container', '-container-0-', True)]
currentContainer = containers[0]
scope = 0
for i in range(1, 24):
    containers.append(Container('New container', f'-container-{i}-', False))

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
            handle_containers_visibility(window, containers)
        else:
            sg.popup_ok('You reached the limits of containers')
    # Remove container
    if event == '-remove-container-':
        if currentContainer is not containers[0]:
            key = currentContainer.key
            containers.remove(currentContainer)
            containers.append(Container('New container', key, False))
            SectionHandler.clear_all_inputs(window)
            currentContainer = containers[0]
            handle_containers_visibility(window, containers)
        else:
            sg.popup_ok('You cannot removed this container')
    # import yaml
    if event == '-import-file-':
        containers = SectionHandler.handle_import_button(window, containers)
        handle_containers_visibility(window, containers)
        currentContainer = containers[0]
        window['-curr-container-'].update(f'Selected container: {currentContainer.name}')
    # Generate YAML
    window['-input-'].update(Generator.GenerateYaml(containers))
    # Update GUI
    Layout.update_gui(window,currentContainer)

window.close()
