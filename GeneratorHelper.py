class GeneratorHelper:
    endline = '\n'
    indent = '   '

    @staticmethod
    def SetContainerName(selected_container, containers, container_name):
        for container in containers:
            if container is selected_container:
                print(container.name)
                selected_container.name = container_name
                break

    @staticmethod
    def SetContainerBuild(selected_container, containers, container_build):
        for container in containers:
            if container is selected_container:
                print(container.name)
                selected_container.build = container_build
                break

    @staticmethod
    def GenerateYaml(containers):
        endline = '\n'
        indent = '   '
        docker_compose = ''
        for container in containers:
            docker_compose += container.name + ':' + endline
        return docker_compose
