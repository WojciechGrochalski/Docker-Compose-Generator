class Depends:
    def __init__(self, dependency):
        self.depends = []
        self.depends.extend(dependency)


class Dependency:
    def __init__(self, dependency):
        self.port = f'- {dependency}'
