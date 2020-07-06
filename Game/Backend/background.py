class Background(object):
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.images = images

        self.frame = 0
        self.currentImage = self.images[self.frame]

    def move(self, speed):
        self.x -= speed

        if self.x == -2400:
            self.x = 2400