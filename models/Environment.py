class Environment:
    def __init__(self, environment):
        if environment:
            self.enviroment = f'  - {environment}"'
        else:
            self.enviroment = ''
