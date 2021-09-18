class Depends:
    def __init__(self, dependency):
        self.depends = dependency


class Dependency:
    def __init__(self, dependency):
        self.depend = f'  - {dependency}'
