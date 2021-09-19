class Dependency:
    def __init__(self, dependency):
        if dependency:
            self.depend = f'  - {dependency}'
        else:
            self.depend = ''
