class Dinosaur(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def jump(self, jumpCount):
        self.y -= (jumpCount * abs(jumpCount)) * 0.2