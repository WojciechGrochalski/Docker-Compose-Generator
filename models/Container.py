from models.Build import Build


class Container:
    def __init__(self, name, image=None, build=None, ports=None, environment=None, depends=None):
        self.name = name
        self.image = image
        self.build = build
        self.ports = ports
        self.environment = environment
        self.depends = depends
