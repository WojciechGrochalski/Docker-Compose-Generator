endline = '\n'
indent = '   '


class Generator:

    @staticmethod
    def get_ports(container):
        container_ports = ''
        for port in container.ports:
            container_ports += port + endline + indent
        return container_ports

    @staticmethod
    def get_environments(container):
        container_environment = ''
        for environment in container.environments:
            container_environment += environment + endline + indent
        return container_environment

    @staticmethod
    def get_dependency(container):
        container_dependency = ''
        for dependency in container.depends:
            container_dependency += dependency + endline + indent
        return container_dependency

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
        docker_compose = ''
        for container in containers:
            docker_compose += container.name + ':' + endline
            # Ports
            if container.ports is not None and container.portsCount > 0:
                docker_compose += indent + 'ports:' + endline
                docker_compose += indent + Generator.get_ports(container) + endline
            # Environments
            if container.environments is not None and container.environmentsCount > 0:
                docker_compose += indent + 'environment:' + endline
                docker_compose += indent + Generator.get_environments(container) + endline
            # Dependency
            if container.depends is not None and container.dependsCount > 0:
                docker_compose += indent + 'depends_on:' + endline
                docker_compose += indent + Generator.get_dependency(container) + endline
        return docker_compose
