class MyTv:


    def __init__(self):
        self.isOn = True
        self.volume = 0
        self.maxVolume = 100
        self.channel = 0
        self.channelDown = 20
        self.mute_channel = True

    def on_myTv(self):
           self.isOn = True

    def inCrease_volume(self):
        if self.isOn and self.volume <= self.maxVolume:
            self.volume +=1

    def deCrease_volume(self):
        if self.isOn and self.volume < self.maxVolume:
            self.volume -=1

    def channel_down(self):
        if self.isOn and self.channel < self.channelDown:
            self.channel -=1

    def channel_up(self):
        if self.isOn and self.channel < self.channelDown:
            self.channel += 1

    def set_channel(self, value):
        self.channel = value

    def mute_channell(self)->bool:
        if self.isOn:
            return self.mute_channel

    def unMute_channell(self) -> bool:
        if self.isOn:
            if self.mute_channel == True:
                self.mute_channel = False


















