import pygame as pg
import os

import Backend.dinosaur as objDinosaur
import Backend.cactu as objCactu
import Backend.bird as objBird

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[443, 0, 37, 72], [480, 0, 34, 72], [514, 0, 34, 72], [548, 0, 34, 72],
                     [582, 0, 34, 72], [616, 0, 35, 72], [651, 0, 51, 102], [702, 0, 49, 102],
                     [751, 0, 52, 102], [803, 0, 47, 102], [850, 0, 102, 102]]

DINOSAUR_DIMENSIONS = [[75, 0, 90, 96], [1338, 0, 88, 96], [1426, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1690, 0, 88, 96], [1778, 0, 88, 96], [1866, 0, 118, 96], [1984, 0, 120, 96]]

PTERODACTYL_DIMENSIONS = [[259, 0, 93, 84], [352, 0, 92, 84]]

def loadImage(imageName):
    try:
        image = pg.image.load(DIC_PATH + imageName)
    except pg.error:
        print("Cannot load image: ", imageName)
        raise SystemExit
    return image, image.get_rect()

def createTrex(xInitial, yInitial, imageAll):
    imagesDino = []
    for dimension in DINOSAUR_DIMENSIONS:
        imagesDino.append(imageAll.subsurface(dimension))
    return objDinosaur.Dinosaur(xInitial, yInitial, imagesDino)

def createBird(xInitial, yInitial, imageAll):
    imagesBird = []
    for dimension in PTERODACTYL_DIMENSIONS:
        imagesBird.append(imageAll.subsurface(dimension))
    return objBird.Bird(xInitial, yInitial, imagesBird)

def createCactu(xInitial, yInitial, imageAll):
    imagesCactu = []
    for dimension in CACTUS_DIMENSIONS:
        imagesCactu.append(imageAll.subsurface(dimension))
    return objCactu.Cactu(xInitial, yInitial, imagesCactu)

def animation(screen, TRex, bird, cactu):
    screen.fill((255, 255, 255)) # preenche a tela com a cor branca
    screen.blit(TRex.currentImage, [TRex.x, TRex.y])
    screen.blit(bird.currentImage, [bird.x, bird.y])
    screen.blit(cactu.currentImage, [cactu.x, cactu.y])
    pg.display.update()

def render():
    pg.init()

    close = False
    
    screen = pg.display.set_mode((800, 600)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    imageAll, dimensionsAll = loadImage("/assets/imageGeneral.png")
    # imageSmall = pg.transform.scale(image, [72, 72])

    TRex = createTrex(50, 350, imageAll)
    bird = createBird(300, 350, imageAll)
    cactu = createCactu(450, 350, imageAll)

    isJump = False
    jumpCount = 10

    countFrameDino = 0
    countFrameBird = 0
    # countFrameCactu = 0

    while close != True:
        pg.time.delay(20)

        animation(screen, TRex, bird, cactu)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()
        
        if keys[pg.K_ESCAPE]:
            close = True

        if keys[pg.K_UP]:
            isJump = True

        if isJump:
            if jumpCount >= -10:
                TRex.jump(jumpCount)
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
                TRex.walk()
        else:
            # timeout
            if countFrameDino > 3:
                TRex.walk()
                countFrameDino = 0
            countFrameDino += 1

        if countFrameBird > 15:
            bird.fly()
            countFrameBird = 0
        countFrameBird += 1

    pg.quit()

render()
