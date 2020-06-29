import pygame as pg
import os

import Backend.dinosaur as objDinosaur
import Backend.cactu as objCactu
import Backend.bird as objBird

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

CACTUS_DIMENSIONS = [[443, 0, 37, 72], [480, 0, 68, 72], [548, 0, 102, 72],
                     [651, 0, 51, 102], [702, 0, 102, 102], [803, 0, 150, 102]]

DINOSAUR_DIMENSIONS = [[75, 0, 90, 96], [1338, 0, 88, 96], [1426, 0, 88, 96], [1514, 0, 88, 96], [1602, 0, 88, 96],
                       [1690, 0, 88, 96], [1778, 0, 88, 96], [1866, 0, 118, 96], [1984, 0, 120, 96]]

PTERODACTYL_DIMENSIONS = [[259, 0, 93, 84], [352, 0, 92, 84]]

def loadImages(imageName):
    try:
        imageAll = pg.image.load(DIC_PATH + imageName)
        imageDino = [imageAll.subsurface(dimension) for dimension in DINOSAUR_DIMENSIONS]
        imagesBird = [imageAll.subsurface(dimension) for dimension in PTERODACTYL_DIMENSIONS]
        imagesCactu = [imageAll.subsurface(dimension) for dimension in CACTUS_DIMENSIONS]
    except pg.error:
        print("Cannot load image: ", imageName)
        raise SystemExit
    return imageDino, imagesBird, imagesCactu
    
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

    imageDino, imagesBird, imagesCactu = loadImages("/assets/imageGeneral.png")
    # imageSmall = pg.transform.scale(image, [72, 72])

    TRex = objDinosaur.Dinosaur(50, 350, imageDino)
    bird = objBird.Bird(300, 350, imagesBird)
    cactu = objCactu.Cactu(450, 350, imagesCactu)

    isJump = False
    isDown = False
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
        else:
            # timeout
            if countFrameDino > 3:
                TRex.walk()
                countFrameDino = 0
            countFrameDino += 1

        # timeout
        # bird.move()
        if countFrameBird > 15:
            bird.fly()
            countFrameBird = 0
        countFrameBird += 1

        # cactu.move()
        # cactu.changeCurrentImage()

    pg.quit()

render()
