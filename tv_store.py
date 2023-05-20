class TV:
    def __init__(self, name='TV', channel=20, volume_level=3, on=True, brand='Brand X'):
        self.name = name
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.brand = brand
        # conditions to set channel limit and volume level limit
        if volume_level > 7 or volume_level < 1:
            print('You can only pick between level 1 to 7 of volume level.')
        if channel > 120 or channel < 1:
            print('You can only pick between channels 1 to 120.')
    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True
    def get_channel(self):
        print('Channel: ' + str(self.channel))
    def set_channel(self, channel):
        # prevents the user from picking outside the channel limit
        if channel > 120 or channel < 1:
            print('You can only pick between channels 1 to 120.')
        else:
            self.channel = channel
    def get_volume(self):
        print('Volume level: ' + str(self.volume_level))
    def set_volume(self, volume_level):
        # prevents the user from picking outside the volume level limit
        if volume_level > 7 or volume_level < 1:
            print('You can only pick between level 1 to 7 of volume level.')
        else:
            self.volume_level = volume_level
    def channel_up(self):
        # the TV will loop back to channel 1 when the upper limit is reached
        # as seen in some models of TV
        if self.channel == 120:
            self.channel = 1
        else:
            self.channel += 1
    def channel_down(self):
        # the TV will go to the upper channel limit when the lower limit is reached
        # just like in some models of TV
        if self.channel == 1:
            self.channel = 120
        else:
            self.channel -= 1
    def volume_up(self):
        # TVs do not let user go past from the upper limit of volume level
        # so, the volume level would stay the same
        if self.volume_level == 7:
            print('You have reached the limit of volume levels')
            self.volume_level = 7
        else:
            self.channel += 1
    def volume_down(self):
        # TVs do not let user go past from the upper limit of volume level
        # so, the volume level would stay the same
        if self.volume_level == 1:
            print('You have reached the limit of volume levels')
            self.volume_level = 1
        else:
            self.channel -=1 
    def display(self):
        print(self.name + "'s channel is " + str(self.channel) + ' and volume level is ' + str(self.volume_level))
        # 'Brand X' would serve as the generic brand for the TV if user did not label
        # what specific brand the TV has
        if self.brand == 'Brand X':
            print('It is a generic brand of TV.')
        else:
            print('It is a ' + self.brand + ' TV.')
        if self.on == True:
            print('The TV is currently on.\n')
        else:
            print('The TV is currently off.\n')