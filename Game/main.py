import pygame as pg
import os

import Backend.dinosaur as dino

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

# Function Load Image
def load_image(image_name):
    """Carrega uma imagem na memoria"""
    # fullname = pg.image.load(DIC_PATH + "/assets/dino.png")
    try:
        image = pg.image.load(DIC_PATH + image_name)
    except pg.error:
        print("Cannot load image: ", image_name)
        raise SystemExit
    return image, image.get_rect()

def animation(screen, image, position):
    screen.fill((255, 255, 255)) # preenche a tela com a cor branca
    screen.blit(image, position)
    pg.display.update()

def render():
    pg.init()

    screen = pg.display.set_mode((600, 600)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    image, dimensions = load_image("/assets/dino.png")
    imageSmall = pg.transform.scale(image, [64, 64])
    trex = dino.Dinosaur(0, 350, imageSmall)

    close = False
    isJump = False
    jumpCount = 10
    position = [0, 350, 20, 50]

    while close != True:
        pg.time.delay(20)
        animation(screen, trex.image, [trex.x, trex.y])

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
                trex.jump(jumpCount)
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

    pg.quit()

render()
