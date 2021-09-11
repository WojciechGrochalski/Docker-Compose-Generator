class Ports:
    def __init__(self, ports):
        self.ports = []
        self.ports.extend(ports)


class Port:
    def __init__(self, output_port, input_port):
        self.port = f'"{output_port}:{input_port}"'
