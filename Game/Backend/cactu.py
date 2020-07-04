class Cactu(object):
    def __init__(self, images):
        self.x = 500
        self.y = 0
        self.speed = 5
        self.images = images

        self.frame = 5
        self.currentImage = self.images[self.frame]

    def calculateCoordinates(self, background):
        dimensionsCactu = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsCactu[3]
        # self.x = background.x

    def move(self):
        self.x -= self.speed
    
    def changeCurrentImage(self):
        self.frame += 1
        if self.frame == len(self.images):
            self.frame = 0

        self.currentImage = self.images[self.frame]