endLine = '\n'
indent = '   '


class Generator:
    version = '3.8'

    @staticmethod
    def get_ports(container):
        container_ports = ''
        for port in container.ports:
            if port:
                if port is container.ports[0]:
                    container_ports += port + endLine
                else:
                    container_ports += indent * 2 + port + endLine
        return container_ports

    @staticmethod
    def get_environments(container):
        container_environment = ''
        for environment in container.environments:
            if environment:
                if environment is container.environments[0]:
                    container_environment += environment + endLine
                else:
                    container_environment += indent * 2 + environment + endLine
        return container_environment

    @staticmethod
    def get_dependency(container):
        container_dependency = ''
        for dependency in container.depends:
            if dependency:
                if dependency is container.depends[0]:
                    container_dependency += dependency + endLine
                else:
                    container_dependency += indent * 2 + dependency + endLine
        return container_dependency

    @staticmethod
    def get_build(container):
        container_build = ''
        if container.build:
            container_build += indent * 3 + 'context: ' + container.build.context + endLine
            container_build += indent * 3 + 'dockerfile: ' + container.build.dockerfile + endLine
        return container_build

    @staticmethod
    def get_image(container):
        container_image = ''
        if container.image:
            container_image += container.image + endLine
        return container_image

    @staticmethod
    def get_volumes(container):
        volumes = ''
        for volume in container.volumes:
            if volume:
                if volume is container.volumes[0]:
                    volumes += volume + endLine
                else:
                    volumes += indent * 2 + volume + endLine
        return volumes


    @staticmethod
    def SetContainerName(selected_container, containers, container_name):
        for container in containers:
            if container is selected_container:
                selected_container.name = container_name
                break

    @staticmethod
    def SetContainerBuild(selected_container, containers, container_build):
        for container in containers:
            if container is selected_container:
                selected_container.build = container_build
                break

    @staticmethod
    def GenerateYaml(containers):
        docker_compose = f'\nversion:  "{Generator.version}"' + endLine * 2 + 'services:' + endLine * 2
        for container in containers:
            if container.active:
                docker_compose += indent + container.name + ':' + endLine
                # Image
                if container.image is not None:
                    docker_compose += indent * 2 + 'image: ' + Generator.get_image(container)
                    # Build
                if container.build is not None:
                    docker_compose += indent * 2 + 'build:' + endLine + Generator.get_build(container)
                    # Ports
                if container.ports is not None and container.portsCount > 0 \
                        and len(container.ports[0]) > 0:
                    docker_compose += indent * 2 + 'ports:' + endLine
                    docker_compose += indent * 2 + Generator.get_ports(container)
                # Environments
                if container.environments is not None and container.environmentsCount > 0 \
                        and len(container.environments[0]) > 0:
                    docker_compose += indent * 2 + 'environment:' + endLine
                    docker_compose += indent * 2 + Generator.get_environments(container)
                # Dependency
                if container.depends is not None and container.dependsCount > 0 \
                        and len(container.depends[0]) > 0:
                    docker_compose += indent * 2 + 'depends_on:' + endLine
                    docker_compose += indent * 2 + Generator.get_dependency(container)
                # Volumes
                if container.volumes is not None and container.volumesCount > 0 \
                        and len(container.volumes[0]) > 0:
                    docker_compose += indent * 2 + 'volumes:' + endLine
                    docker_compose += indent * 2 + Generator.get_volumes(container)

                docker_compose += endLine
        return docker_compose
