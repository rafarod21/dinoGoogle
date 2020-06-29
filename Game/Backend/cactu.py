class Cactu(object):
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.speed = 5
        self.images = images

        self.frame = 0
        self.currentImage = self.images[self.frame]

    def move(self):
        self.x -= self.speed
    
    def changeCurrentImage(self):
        self.frame += 1
        if self.frame == len(self.images):
            self.frame = 0

        self.currentImage = self.images[self.frame]