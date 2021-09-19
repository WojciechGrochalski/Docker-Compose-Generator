from GeneratorHelper import Generator
from layout import Layout
from layout.Sections.DependencySection import save_depends_section, clear_dependency_section
from layout.Sections.EnvironmentSection import save_env_section, clear_environment_section
from layout.Sections.NameSection import save_container_name_section
from layout.Sections.PortSection import save_port_section, clear_port_section


class SectionHandler:

    @staticmethod
    def handle_all_section(event, values, window, container, containers):
        # Controls
        SectionHandler.handle_controls_section(event, window, values, container, containers)
        # Name
        SectionHandler.handle_name_section(event, window, values, container)
        # Ports
        SectionHandler.handle_port_section(event, values, container)
        # Environment
        SectionHandler.handle_env_section(event, values, container)
        # Dependency
        SectionHandler.handle_depends_section(event, values, container)

    @staticmethod
    def handle_controls_section(event, window, values, currnet_container, containers):
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
    def handle_env_section(event, values, container):
        if event == '-save-env-':
            save_env_section(values, container)

    @staticmethod
    def handle_name_section(event, window, values, container):
        if event == '-save-name-':
            save_container_name_section(values, window, container)

    @staticmethod
    def handle_port_section(event, values, container):
        if event == '-save-port-':
            save_port_section(values, container)

    @staticmethod
    def handle_depends_section(event, values, container):
        if event == '-save-depends-':
            save_depends_section(values, container)

    @staticmethod
    def clear_all_inputs(window):
        clear_port_section(window)
        clear_environment_section(window)
        clear_dependency_section(window)




