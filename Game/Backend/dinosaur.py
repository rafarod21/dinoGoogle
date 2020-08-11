import pygame as pg

class Dinosaur(object):
    def __init__(self, images, gameSize):
        self.x = gameSize[0] + 50
        self.y = 0
        self.images = images

        self.frame = 0
        self.dinoStop = [self.images[0]]
        self.dinoWalk = [self.images[3], self.images[4]]
        self.dinoDown = [self.images[7], self.images[8]]
        self.dinoJump = [self.images[1]]
        self.dinoDead = [self.images[5]]

        self.currentImage = self.dinoStop[self.frame]

    def settingsAccordingScreen(self, gameSize):
        # Redimensionar as imagens
        # Calcular a posição inicial (função abaixo)
        # Calcular o tamanho máximo do pulo
        return

    def calculateInitialCoordinates(self, background):
        dimensionsDino = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsDino[3] + 6
        self.yInitial = self.y

    def calculateCoordinates(self, background):
        dimensionsDino = self.currentImage.get_rect()
        dimensionsBackground = background.currentImage.get_rect()

        self.y = background.y + dimensionsBackground[3] - dimensionsDino[3]
        self.yInitial = self.y
        # self.x = background.x

    def walk(self):
        self.currentImage = self.dinoWalk[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1

    def jump(self, jumpCount):
        self.y -= jumpCount * 0.3
        self.currentImage = self.dinoJump[0]
        
    def down(self):
        self.currentImage = self.dinoDown[self.frame]

        if self.frame:
            self.frame = 0
        else:
            self.frame = 1

    def colied(self, listObj):
        listObjAux = []
        for obj in listObj:
            listObjAux.append([obj.x, obj.y, obj.dimensions[2]-10, obj.dimensions[3]])

        coordinatesDino = pg.Rect(self.x, self.y, self.currentImage.get_rect()[2], self.currentImage.get_rect()[3])
        if coordinatesDino.collidelist(listObjAux) >= 0:
            print("************** Colidiu **************");
            return True