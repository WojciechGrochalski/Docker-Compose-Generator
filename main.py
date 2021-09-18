import PySimpleGUI as sg
import randomname
from GeneratorHelper import Generator
from handlers.SectionHandler import SectionHandler
from models.Container import Container
from layout import Layout


containers = [Container('Raven', randomname.get_name()),
              Container('redis', randomname.get_name()),
              Container('mongoDb', randomname.get_name())]

sg.theme('DarkTanBlue')

window = sg.Window('Docker-Compose Generator', size=(1200, 800), resizable=True,
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT).layout(Layout.create_layout(containers))
currnetContainer = None
while True:
    event, values = window.read()
    window['-input-'].update(Generator.GenerateYaml(containers))
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if Layout.is_set_container(containers, event):
        # Set currnet container
        currnetContainer = Layout.set_current_container(containers, event, window)
        # set boot options
        SectionHandler.handle_start_visibility_of_all_section(window, currnetContainer)
        SectionHandler.clear_all_inputs(window)
        window.refresh()

    # Handle sections
    SectionHandler.handle_all_section(event, values, window, currnetContainer, containers)
    # Generate yaml
    window['-input-'].update(Generator.GenerateYaml(containers))
    # Visibility
    SectionHandler.handle_all_button_visibility(window, currnetContainer)
    # Add container
    if event == '-add-container-':
        containers.append(Container('Nowy', randomname.get_name()))
        window1 = sg.Window('Docker-Compose Generator', size=(1200, 800), resizable=True,
                            right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT).layout(Layout.create_layout(containers))
        window.Close()
        window = window1

window.close()
