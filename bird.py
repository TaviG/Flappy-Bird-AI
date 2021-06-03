class Bird:  #Bird Class
    x=45
    y=250
    birdindex=0
    tick_count=0
    counter=0
    vel = 0
    height=y

    def jump(self): #Jump function
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y