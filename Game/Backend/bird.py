class Bird(object):
    def __init__(self, x, images):
        self.x = x
        self.y = 0
        self.images = images

        self.frame = 0
        self.currentImage = self.images[self.frame]

    def calculateCoordinates(self, background):
        dimensionsBird = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsBird[3]
        # self.x = background.x

    def move(self, speed):
        self.x -= speed

    def fly(self):
        self.currentImage = self.images[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1