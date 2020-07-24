class Background(object):
    def __init__(self, images, gameSize, controll):
        self.images = images
        self.frame = 0
        self.currentImage = self.images[self.frame]
        self.imageDimensions = self.currentImage.get_rect()

        self.x = gameSize[0] + (controll * self.imageDimensions[2])
        self.y = gameSize[1] + (gameSize[3]/5 *4)

    def move(self, speed, gameSize):
        self.x -= speed

        if self.x == -self.imageDimensions[2] + gameSize[0]:
            self.x = self.imageDimensions[2] + gameSize[0]