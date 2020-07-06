import random

class Cactu(object):
    def __init__(self, x, images):
        self.xInitial = x
        self.x = self.xInitial
        self.y = 0
        self.images = images

        self.frame = 5
        self.currentImage = self.images[self.frame]
        self.dimensionsCactu = self.currentImage.get_rect()

    def calculateCoordinates(self, background):
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - self.dimensionsCactu[3]
        # self.x = background.x

    def move(self, speed):
        self.x -= speed

        if self.x < -self.dimensionsCactu[2]:
            self.x = self.xInitial
    
    def changeCurrentImage(self):
        image = random.randint(0, 5)
        print(image)
        self.currentImage = self.images[image]
        self.dimensionsCactu = self.currentImage.get_rect()