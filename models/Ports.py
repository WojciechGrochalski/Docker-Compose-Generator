class Port:
    def __init__(self, output_port, input_port):
        if output_port and input_port:
            self.port = f'  - "{output_port}:{input_port}"'
        else:
            self.port = ''
