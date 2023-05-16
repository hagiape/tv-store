class TV:
    def __init__(self, brand='Brand X', channel='20', volume_level=3, on=True):
        self.brand = brand
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True