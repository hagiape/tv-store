class TV:
    def __init__(self, name='TV', channel=20, volume_level=3, on=False, brand='Brand X'):
        self.name = name
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.brand = brand
        if volume_level > 7 or volume_level < 1:
            print('You can only pick between level 1 to 7 of volume level.')
            self.volume_level = 3
        if channel > 120 or channel < 1:
            print('You can only pick between channels 1 to 120.')
            self.channel = 20
    def volume_limit(self):
        print('You can only pick between level 1 to 7 of volume level.')
        self.volume_level = 3
    def channel_limit(self):
        print('You can only pick between channels 1 to 120.')
        self.displaychannel = 20
    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        if channel > 120 or channel < 1:
            self.channel_limit()
        else:
            self.channel = channel
    def get_volume(self):
        return self.volume_level
    def set_volume(self, volume_level):
        if volume_level > 7 or volume_level < 1:
            self.volume_limit()
        else:
            self.volume_level = volume_level
    def channel_up(self):
        if self.channel > 120 or self.channel < 1:
            self.channel_limit()
        else:
            self.channel += 1
    def channel_down(self):
        if self.channel > 120 or self.channel < 1:
            self.channel_limit()
        else:
            self.channel -= 1
    def volume_up(self):
        if self.volume > 120 or self.volume < 1:
            self.volume_limit()
        else:
            self.channel += 1
    def volume_down(self):
        if self.volume > 120 or self.volume < 1:
            self.volume_limit()
        else:
            self.channel -=1 
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