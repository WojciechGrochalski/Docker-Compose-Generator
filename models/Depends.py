class Dependency:
    def __init__(self, dependency):
        if dependency:
            self.dependency = f'  - {dependency}'
        else:
            self.dependency = ''
