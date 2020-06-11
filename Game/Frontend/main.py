import pygame as pg

def animation(tela, tupla):
    tela.fill((255, 255, 255)) # preenche a tela com a cor branca
    pg.draw.line(tela, (0, 0, 0), (0, 400), (400, 400))
    pg.draw.rect(tela, (0, 0, 0), tupla)

def screen():
    pg.init()
    tela = pg.display.set_mode((600, 600)) # largura / altura
    pg.display.set_caption("T-Rex Running")
    close = False
    controlJump = True
    position = [0, 350, 20, 50]

    while close != True:
        animation(tela, position)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_UP:
                    print("Cima")
                    if controlJump:
                        position[1] = 300
                        controlJump = False
                
                if event.key == pg.K_DOWN:
                    print("Baixo")
                    if not controlJump:
                        position[1] = 350
                        controlJump = True
                
                if event.key == pg.K_SPACE:
                    print("Espaço")
                    close = True
 
            pg.display.update()

        # pg.time.delay(100)

    pg.quit()

screen()
