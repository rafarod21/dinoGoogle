class Dinosaur(object):
    def __init__(self, x, images):
        self.x = x
        self.y = 0
        self.images = images

        self.frame = 0
        self.dinoStop = [self.images[0]]
        self.dinoWalk = [self.images[3], self.images[4]]
        self.dinoDown = [self.images[7], self.images[8]]
        self.dinoJump = [self.images[1]]
        self.dinoDead = [self.images[5]]

        self.currentImage = self.dinoStop[self.frame]

    def calculateInitialCoordinates(self, background):
        dimensionsDino = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsDino[3] + 6

    def calculateCoordinates(self, background):
        dimensionsDino = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsDino[3]
        # self.x = background.x

    def walk(self):
        self.currentImage = self.dinoWalk[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1

    def jump(self, jumpCount):
        self.y -= (jumpCount * abs(jumpCount)) * 0.6
        self.currentImage = self.dinoJump[0]

    def down(self):
        self.currentImage = self.dinoDown[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1