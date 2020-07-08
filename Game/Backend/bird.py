class Bird(object):
    def __init__(self, x, images):
        self.xInitial = x
        self.x = self.xInitial
        self.y = 0
        self.images = images

        self.frame = 0
        self.currentImage = self.images[self.frame]
        self.dimensionsBird = self.currentImage.get_rect()

    def calculateCoordinates(self, background):
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - self.dimensionsBird[3]
        # self.x = background.x

    def move(self, speed):
        self.x -= speed

        if self.x < -self.dimensionsBird[2]:
            self.x = self.xInitial

    def fly(self):
        self.currentImage = self.images[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1