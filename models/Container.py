class Container:
    def __init__(self, name, key, active=False, image=None, build=None, ports=None, environments=None, dependency=None,
                 volumes=None):
        self.name = name
        self.key = key
        self.image = image
        self.build = build
        self.ports = ports
        self.environments = environments
        self.dependency = dependency
        self.volumes = volumes
        self.portsCount = 0
        self.environmentsCount = 0
        self.dependsCount = 0
        self.volumesCount = 0
        self.active = active
