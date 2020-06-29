class Bird(object):
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.speed = 5
        self.images = images

        self.frame = 0
        self.currentImage = self.images[self.frame]

    def move(self):
        self.x -= self.speed

    def fly(self):
        self.currentImage = self.images[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1