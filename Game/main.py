import pygame as pg
import os

import Backend.dinosaur as objDinosaur
import Backend.cactu as objCactu
import Backend.bird as objBird
import Backend.background as objBackground

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[446, 0, 34, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [652, 0, 50, 102], [702, 0, 102, 102], [802, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[76, 6, 90, 96], [1338, 2, 88, 94], [1426, 2, 88, 94], [1514, 2, 88, 94], [1602, 2, 88, 94],
                       [1690, 2, 88, 94], [1782, 6, 80, 86], [1866, 36, 118, 60], [1984, 36, 118, 60]]

PTERODACTYL_DIMENSIONS = [[260, 0, 93, 84], [352, 0, 92, 84]]

BACKGROUND_DIMENSIONS = [[2, 104, 2400, 24]]

def loadImages(imageName):
    try:
        imageAll = pg.image.load(DIC_PATH + imageName)
        imagesDino = [imageAll.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
        imagesBird = [imageAll.subsurface(dimension) for dimension in PTERODACTYL_DIMENSIONS]
        imagesCactu = [imageAll.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
        imageBackground = [imageAll.subsurface(dimension) for dimension in BACKGROUND_DIMENSIONS]
    except pg.error:
        print("Cannot load image: ", imageName)
        raise SystemExit
    return imagesDino, imagesBird, imagesCactu, imageBackground

def getImagesDimensions(imagesDino, imagesBird, imagesCactu, imageBackground):
    dimensionsDino = [image.get_rect() for image in imagesDino]
    dimensionsBird = [image.get_rect() for image in imagesBird]
    dimensionsCactu = [image.get_rect() for image in imagesCactu]
    dimensionsBackground = [image.get_rect() for image in imageBackground]
    return dimensionsDino, dimensionsBird, dimensionsCactu, dimensionsBackground
    
def animation(screen, TRex, bird, cactu, background1, background2):
    screen.fill((255, 255, 255)) # preenche a tela com a cor branca
    screen.blit(background1.currentImage, [background1.x, background1.y])
    screen.blit(background2.currentImage, [background2.x, background2.y])
    screen.blit(TRex.currentImage, [TRex.x, TRex.y])
    screen.blit(bird.currentImage, [bird.x, bird.y])
    screen.blit(cactu.currentImage, [cactu.x, cactu.y])
    pg.display.update()

def render():
    pg.init()

    close = False
    
    screen = pg.display.set_mode((800, 600)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    imagesDino, imagesBird, imagesCactu, imageBackground = loadImages("/assets/imageGeneral.png")
    dimensionsDino, dimensionsBird, dimensionsCactu, dimensionsBackground = getImagesDimensions(imagesDino, imagesBird, imagesCactu, imageBackground)
    # imageSmall = pg.transform.scale(image, [72, 72])

    TRex = objDinosaur.Dinosaur(50, imagesDino)
    bird = objBird.Bird(300, imagesBird)
    cactu = objCactu.Cactu(imagesCactu)
    background1 = objBackground.Background(0, 420, imageBackground)
    background2 = objBackground.Background(2400, 420, imageBackground)

    isJump = False
    isDown = False
    jumpCount = 10

    countFrameDino = 0
    countFrameBird = 0
    # countFrameCactu = 0

    # TRex.calculateInitialCoordinates(background1)
    TRex.calculateCoordinates(background1)

    while close != True:
        cactu.calculateCoordinates(background1)
        bird.calculateCoordinates(background1)
        pg.time.delay(20)

        animation(screen, TRex, bird, cactu, background1, background2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()
        
        if keys[pg.K_ESCAPE]:
            close = True

        if keys[pg.K_UP]:
            isJump = True

        if keys[pg.K_DOWN]:
            isDown = True
        else:
            isDown = False

        if isJump:
            if jumpCount >= -10:
                TRex.jump(jumpCount)
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
                TRex.walk()
        elif isDown:
            # timeout
            if countFrameDino > 3:
                TRex.down()
                countFrameDino = 0
            countFrameDino += 1
            TRex.calculateCoordinates(background1)
        else:
            # timeout
            if countFrameDino > 3:
                TRex.walk()
                countFrameDino = 0
            countFrameDino += 1
            TRex.calculateCoordinates(background1)

        # timeout
        # bird.move()
        if countFrameBird > 15:
            # cactu.changeCurrentImage()
            bird.fly()
            countFrameBird = 0
        countFrameBird += 1

        # cactu.move()

        # background1.move()
        # background2.move()

    pg.quit()

render()
