class Volume:
    def __init__(self, volume):
        if volume:
            self.volume = f'  - {volume}'
        else:
            self.volume = ''
