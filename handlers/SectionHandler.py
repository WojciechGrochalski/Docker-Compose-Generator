from GeneratorHelper import Generator
from layout import MenuLayout, Layout


class SectionHandler:
    @staticmethod
    def handle_controls_section(event, values, window, currnet_container, containers):
        if event == '-save-image-':
            Generator.SetContainerName(currnet_container, containers, values['-image-name-value-'])
        if event == '-name-':
            Layout.toggleVisibilityOfSectionName(window, True)
        if event == '-image-':
            Layout.toggleVisibilityOfSectionImage(window, True)
        if event == '-build-':
            Layout.toggleVisibilityOfSectionBuild(window, True)
        if event == '-ports-':
            Layout.toggleVisibilityOfSectionPort(window, True)
        if event == '-env-':
            Layout.toggleVisibilityOfSectionEnv(window, True)
        if event == '-depends-':
            Layout.toggleVisibilityOfSectionDepends(window, True)

    @staticmethod
    def handle_all_section(event, values, window, container, containers):
        # Controls
        SectionHandler.handle_controls_section(event, values, window, container, containers)
        # Name
        SectionHandler.handle_name_section(event, window, values, container)
        # Ports
        SectionHandler.handle_port_section(event, values, window, container)
        # Environment
        SectionHandler.handle_env_section(event, values, window, container)
        # Dependency
        SectionHandler.handle_depends_section(event, values, window, container)

    @staticmethod
    def toggle_all_section(window, container):
        # Ports
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
        # Enviroments
        MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
        # Dependency
        MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)

    @staticmethod
    def handle_start_visibility_of_all_section(window, container):
        # Controls
        Layout.toggle_visibilit_of_section_controls(window, True)
        # Ports
        MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
        # Enviroments
        MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
        # Dependency
        MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)

    @staticmethod
    def handle_all_button_visibility(window, container):
        # Ports
        SectionHandler.handle_ports_button_visibility(window, container)
        # Enviroments
        SectionHandler.handle_env_button_visibility(window, container)
        # Dependency
        SectionHandler.handle_dependency_button_visibility(window, container)

    @staticmethod
    def handle_ports_button_visibility(window, container, max_range=8):
        if container is not None:
            if container.portsCount == 0:
                window['-remove-port-'].update(visible=False)
            else:
                window['-remove-port-'].update(visible=True)
            if container.portsCount > max_range:
                window['-add-port-'].update(visible=False)
            else:
                window['-add-port-'].update(visible=True)

    @staticmethod
    def handle_env_button_visibility(window, container, max_range=8):
        if container is not None:
            if container.environmentsCount == 0:
                window['-remove-env-'].update(visible=False)
            else:
                window['-remove-env-'].update(visible=True)
            if container.environmentsCount > max_range:
                window['-add-env-'].update(visible=False)
            else:
                window['-add-env-'].update(visible=True)

    @staticmethod
    def handle_dependency_button_visibility(window, container, max_range=8):
        if container is not None:
            if container.dependsCount == 0:
                window['-remove-depends-'].update(visible=False)
            else:
                window['-remove-depends-'].update(visible=True)
            if container.dependsCount > max_range:
                window['-add-depends-'].update(visible=False)
            else:
                window['-add-depends-'].update(visible=True)

    @staticmethod
    def handle_env_section(event, values, window, container):
        if event == '-add-env-':
            container.environmentsCount += 1
            MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
        if event == '-remove-env-':
            container.environmentsCount -= 1
            MenuLayout.toggle_env_in_range(container.environmentsCount, True, window)
        if event == '-save-env-':
            MenuLayout.save_env_section(values, container)

    @staticmethod
    def handle_name_section(event, window, values, container):
        if event == '-save-name-':
            MenuLayout.save_container_name_section(values, window, container)

    @staticmethod
    def handle_port_section(event, values, window, container):
        if event == '-add-port-':
            container.portsCount += 1
            MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
        if event == '-remove-port-':
            container.portsCount -= 1
            MenuLayout.toggle_ports_in_range(container.portsCount, True, window)
        if event == '-save-port-':
            MenuLayout.save_port_section(values, container)

    @staticmethod
    def handle_depends_section(event, values, window, container):
        if event == '-add-depends-':
            container.dependsCount += 1
            MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)
        if event == '-remove-depends-':
            container.dependsCount -= 1
            MenuLayout.toggle_depends_in_range(container.dependsCount, True, window)
        if event == '-save-depends-':
            MenuLayout.save_depends_section(values, container)

    @staticmethod
    def clear_all_inputs(window):
        for i in range(1, 9):
            window[f'-env-value-{i}-'].update('')
            window[f'-depends-value-{i}-'].update('')
            window[f'-outer-port-value-{i}-'].update('')
            window[f'-inner-port-value-{i}-'].update('')
