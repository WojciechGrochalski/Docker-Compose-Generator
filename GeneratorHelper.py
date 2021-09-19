endline = '\n'
indent = '   '


class Generator:
    version = '3.8'

    @staticmethod
    def get_ports(container):
        container_ports = ''
        for port in container.ports:
            if port:
                if port is container.ports[0]:
                    container_ports += port + endline
                else:
                    container_ports += indent * 2 + port + endline
        return container_ports

    @staticmethod
    def get_environments(container):
        container_environment = ''
        for environment in container.environments:
            if environment:
                if environment is container.environments[0]:
                    container_environment += environment + endline
                else:
                    container_environment += indent * 2 + environment + endline
        return container_environment

    @staticmethod
    def get_dependency(container):
        container_dependency = ''
        for dependency in container.depends:
            if dependency:
                if dependency is container.depends[0]:
                    container_dependency += dependency + endline
                else:
                    container_dependency += indent * 2 + dependency + endline
        return container_dependency

    @staticmethod
    def get_build(container):
        container_build = ''
        if container.build:
            container_build += indent * 3 + 'context: ' + container.build.context + endline
            container_build += indent * 3 + 'dockerfile: ' + container.build.dockerfile + endline
        return container_build

    @staticmethod
    def get_image(container):
        container_image = ''
        if container.image:
            container_image += container.image + endline
        return container_image

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
        docker_compose = f'version:  "{Generator.version}"' + endline + 'services:' + endline
        for container in containers:
            if container.active:
                docker_compose += indent + container.name + ':' + endline
                # Image
                if container.image is not None:
                    docker_compose += indent * 2 + 'image: ' + Generator.get_image(container)
                    # Build
                if container.build is not None:
                    docker_compose += indent * 2 + 'build:' + endline + Generator.get_build(container)
                    # Ports
                if container.ports is not None and container.portsCount > 0:
                    docker_compose += indent * 2 + 'ports:' + endline
                    docker_compose += indent * 2 + Generator.get_ports(container)
                # Environments
                if container.environments is not None and container.environmentsCount > 0:
                    docker_compose += indent * 2 + 'environment:' + endline
                    docker_compose += indent * 2 + Generator.get_environments(container)
                # Dependency
                if container.depends is not None and container.dependsCount > 0:
                    docker_compose += indent * 2 + 'depends_on:' + endline
                    docker_compose += indent * 2 + Generator.get_dependency(container)

                docker_compose += endline
        return docker_compose
