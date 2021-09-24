class Environment:
    def __init__(self, environment):
        if environment:
            self.environment = f'  - {environment}'
        else:
            self.environment = ''
