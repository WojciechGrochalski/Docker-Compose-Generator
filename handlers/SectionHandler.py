import PySimpleGUI as sg
import yaml
from yaml.loader import SafeLoader

from GeneratorHelper import Generator
from layout import Layout
from layout.Sections.BuildSection import save_build_section, reset_build_value, clear_build_section
from layout.Sections.ContainerSection import handle_containers_visibility
from layout.Sections.DependencySection import save_depends_section, clear_dependency_section
from layout.Sections.EnvironmentSection import save_env_section, clear_environment_section
from layout.Sections.ImageSection import save_container_image_section, reset_image_value, clear_image_section
from layout.Sections.NameSection import save_container_name_section, clear_name_section
from layout.Sections.PortSection import save_port_section, clear_port_section
from layout.Sections.VersionSection import save_version_section
from layout.Sections.VolumesSection import clear_volume_section, save_volume_section


class SectionHandler:

    @staticmethod
    def handle_all_section(event, values, window, container, containers):
        # Controls TODO add volumines command network
        SectionHandler.handle_controls_section(event, window)
        # Name
        SectionHandler.handle_name_section(event, window, values, container)
        # Build
        SectionHandler.handle_build_section(event, values, window, container)
        # Image
        SectionHandler.handle_image_section(event, values, window, container)
        # Ports
        SectionHandler.handle_port_section(values, container)
        # Environment
        SectionHandler.handle_env_section(values, container)
        # Dependency
        SectionHandler.handle_depends_section(values, container)
        # Version
        SectionHandler.handle_version_section(event, values)
        # Volumes
        SectionHandler.handle_volume_section(values, container)
        # Export file
        SectionHandler.handle_export_button(event, containers)

    @staticmethod
    def handle_controls_section(event, window):
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
        if event == '-volumes-':
            Layout.toggleVisibilityOfSectionVolumes(window, True)
        if event == '-select-version-':
            Layout.toggleVisibilityOfSectionVersion(window, True)

    @staticmethod
    def handle_version_section(event, values):
        if event == '-save-version-':
            save_version_section(values)

    @staticmethod
    def handle_env_section(values, container):
        save_env_section(values, container)

    @staticmethod
    def handle_volume_section(values, container):
        save_volume_section(values, container)

    @staticmethod
    def handle_name_section(event, window, values, container):
        if event == '-save-name-':
            save_container_name_section(values, window, container)

    @staticmethod
    def handle_port_section(values, container):
        save_port_section(values, container)

    @staticmethod
    def handle_depends_section(values, container):
        save_depends_section(values, container)

    @staticmethod
    def handle_image_section(event, values, window, container):
        if event == '-save-image-':
            save_container_image_section(values, window, container)
        if event == '-reset-image-':
            reset_image_value(values, container)

    @staticmethod
    def handle_build_section(event, values, window, container):
        if event == '-save-build-':
            save_build_section(values, window, container)
        if event == '-reset-build-':
            reset_build_value(values, container)

    @staticmethod
    def handle_export_button(event, containers):
        if event == '-export-file-':
            path = sg.popup_get_file('', no_window=True, save_as=True,
                                     file_types=(('YAM', '.yam'), ('YAML', '.yaml')))
            with open(path, 'w') as file:
                file.write(Generator.GenerateYaml(containers))

    @staticmethod
    def handle_import_button(window, containers):
        path = path = sg.popup_get_file('', no_window=True,
                                        file_types=(('YAM', '.yam'), ('YAML', '.yaml')))
        if path != '':
            with open(path, 'r') as file:
                data = yaml.load(file, Loader=SafeLoader)
        path = ''
        new_containers, count = Generator.GetYamlFromFile(window, containers, data)
        if new_containers is not None:
            handle_containers_visibility(window, count - 1, containers)
            return new_containers
        return containers

    @staticmethod
    def clear_all_inputs(window):
        clear_port_section(window)
        clear_environment_section(window)
        clear_dependency_section(window)
        clear_build_section(window)
        clear_image_section(window)
        clear_name_section(window)
        clear_volume_section(window)
