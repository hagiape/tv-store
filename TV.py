class TV:
    def __init__(self, name, channel=20, volume_level=3, on=False, brand='Brand X'):
        self.name = name
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.brand = brand
    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        self.channel = channel
    def get_volume(self):
        return self.volume_level
    def set_volume(self, volume_level):
        self.volume_level = volume_level
    def channel_up(self):
        self.channel+=1
    def channel_down(self):
        self.channel-=1
    def volume_up(self):
        self.channel+=1
    def volume_down(self):
        self.channel-=1
    def display(self):
        print(self.name + "'s channel is " + str(self.channel) + ' and volume level is ' + str(self.volume_level))
        if self.brand == 'Brand X':
            print('It is a generic brand of TV.')
        else:
            print('It is a ' + self.brand + ' TV.')
        if self.on == True:
            print('The TV is currently on.')
        else:
            print('The TV is currently off.')