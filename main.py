import PySimpleGUI as sg
from GeneratorHelper import Generator
from handlers.SectionHandler import SectionHandler
from layout.Sections.ContainerSection import handle_containers_visibility
from models.Container import Container
from layout import Layout

containers = [Container('Container', '-container-0-', True)]
currnetContainer = containers[0]
scope = 0
for i in range(1, 10):
    containers.append(Container('Container', f'-container-{i}-', False))

sg.theme('DarkBlack')
sg.theme_background_color('#232733')
sg.theme_text_element_background_color('#232733')
sg.theme_border_width(0)

window = sg.Window('Docker-Compose Generator', size=(1200, 800), resizable=True,
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT).layout(Layout.create_layout(containers))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if Layout.is_set_container(containers, event):
        # Set currnet container
        currnetContainer = Layout.set_current_container(containers, event, window)
        SectionHandler.clear_all_inputs(window)
        window.refresh()
    window['-input-'].update(Generator.GenerateYaml(containers))
    # Handle sections
    SectionHandler.handle_all_section(event, values, window, currnetContainer, containers)
    # Generate yaml
    window['-input-'].update(Generator.GenerateYaml(containers))
    if event == '-add-container-':
        scope += 1
        containers[scope].active = True
        handle_containers_visibility(window, scope, containers)

    window['-input-'].update(Generator.GenerateYaml(containers))

window.close()
