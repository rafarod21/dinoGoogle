import pygame as pg

def screen():
    pg.init()
    tela = pg.display.set_mode((800, 800)) # largura / altura
    pg.display.set_caption("T-Rex Running")
    color = (255, 255, 255) # cor branca
    close = False

    while close != True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    print("Cima")
                if event.key == pg.K_DOWN:
                    print("Baixo")
                if event.key == pg.K_LEFT:
                    print("Esquerda")
                if event.key == pg.K_RIGHT:
                    print("Direita")
                if event.key == pg.K_SPACE:
                    print("Espaço")
                    close = True

            tela.fill(color) # preenche a tela com a cor branca

            pg.display.update()

    pg.quit()

screen()
