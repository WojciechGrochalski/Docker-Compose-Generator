class Container:
    def __init__(self, name, key, active=False, image=None, build=None, ports=None, environments=None, depends=None):
        self.name = name
        self.key = key
        self.image = image
        self.build = build
        self.ports = ports
        self.environments = environments
        self.depends = depends
        self.portsCount = 1
        self.environmentsCount = 1
        self.dependsCount = 1
        self.active = active
