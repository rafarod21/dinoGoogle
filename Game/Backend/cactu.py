import random

class Cactu(object):
    def __init__(self, images, gameSize):
        self.xInitial = gameSize[0] + gameSize[2] + 1
        self.x = self.xInitial
        self.y = 0
        self.images = images

        self.frame = 5
        self.currentImage = self.images[self.frame]
        self.dimensions = self.currentImage.get_rect()

    def calculateCoordinates(self, background):
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - self.dimensions[3]
        # self.x = background.x

    def move(self, speed, gameSize):
        self.x -= speed

        if self.x < gameSize[0] - self.dimensions[2]:
            self.x = self.xInitial
    
    def changeCurrentImage(self):
        image = random.randint(0, 5)
        self.currentImage = self.images[image]
        self.dimensions = self.currentImage.get_rect()