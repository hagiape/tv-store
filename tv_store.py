class TV:
    def __init__(self, name='TV', channel=20, volume_level=3, on=True, brand='Brand X'):
        self.name = name
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.brand = brand
        if volume_level > 7 or volume_level < 1:
            print('You can only pick between level 1 to 7 of volume level.')
        if channel > 120 or channel < 1:
            print('You can only pick between channels 1 to 120.')
    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        if channel > 120 or channel < 1:
            print('You can only pick between channels 1 to 120.')
        else:
            self.channel = channel
    def get_volume(self):
        return self.volume_level
    def set_volume(self, volume_level):
        if volume_level > 7 or volume_level < 1:
            print('You can only pick between level 1 to 7 of volume level.')
        else:
            self.volume_level = volume_level
    def channel_up(self):
        if self.channel == 120:
            self.channel = 1
        else:
            self.channel += 1
    def channel_down(self):
        if self.channel == 1:
            self.channel = 120
        else:
            self.channel -= 1
    def volume_up(self):
        if self.volume_level == 7:
            print('You have reached the limit of volume levels')
            self.volume_level = 7
        else:
            self.channel += 1
    def volume_down(self):
        if self.volume_level == 1:
            print('You have reached the limit of volume levels')
            self.volume_level = 1
        else:
            self.channel -=1 
    def display(self):
        print(self.name + "'s channel is " + str(self.channel) + ' and volume level is ' + str(self.volume_level))
        if self.brand == 'Brand X':
            print('It is a generic brand of TV.')
        else:
            print('It is a ' + self.brand + ' TV.')
        if self.on == True:
            print('The TV is currently on.\n')
        else:
            print('The TV is currently off.\n')