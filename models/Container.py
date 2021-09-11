from models.Build import Build


class Container:
    def __init__(self, name, build, ports, environment=None, depends=None):
        self.name = name
        self.build = Build(build)
        self.ports = ports
        self.environment = environment
        self.depends = depends

    def __init__(self, name, image, ports, environment=None, depends=None):
        self.name = name
        self.image = image
        self.ports = ports
        self.environment = environment
        self.depends = depends


