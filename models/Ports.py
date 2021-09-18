class Ports:
    def __init__(self, ports):
        self.ports = ports


class Port:
    def __init__(self, output_port, input_port):
        self.port = f'  - "{output_port}:{input_port}"'
