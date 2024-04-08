from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from game import jogo
from ranking import tela_ranking

janela = Window(1920,1080)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
fundo = GameImage("images/back.jpg")

velx = 400
nave = Sprite("images/nave.png")
nave.x = 0
nave.y = 300

logo = Sprite("images/LOGO.png")
logo.x = janela.width / 2 - logo.width / 2
logo.y = 100

jogar = Sprite("buttons/jogar.png")
jogar.x = janela.width / 2 - jogar.width / 2
jogar.y = janela.height / 1.48 + 50

jogarblue = Sprite("buttons/jogarblue.png")
jogarblue.x = janela.width / 2 - jogarblue.width / 2
jogarblue.y = janela.height / 1.48 + 50

rank = Sprite("buttons/rank.png")
rank.x = janela.width / 2 - rank.width / 2
rank.y = janela.height / 1.32 + 50

rankblue = Sprite("buttons/rkblue.png")
rankblue.x = janela.width / 2 - rankblue.width / 2
rankblue.y = janela.height / 1.32 + 50

sair = Sprite("buttons/sair.png")
sair.x = janela.width / 2 - sair.width / 2
sair.y = janela.height / 1.21 + 50

sairblue = Sprite("buttons/sairblue.png")
sairblue.x = janela.width / 2 - sairblue.width / 2
sairblue.y = janela.height / 1.21 + 50


while True:
    fundo.draw()
    nave.x += velx * janela.delta_time()
    if nave.x >= janela.width:
        nave.x = -nave.width

    if (mouse.is_over_object(jogar)):
        jogar.hide()
        jogarblue.draw()
        if (mouse.is_button_pressed(1)):
            jogo()
    else:
        jogar.unhide()

    if (mouse.is_over_object(rank)):
        rank.hide()
        rankblue.draw()
        if (mouse.is_button_pressed(1)):
            pontos = [-1]
            tela_ranking(pontos)
    else:
        rank.unhide()

    if (mouse.is_over_object(sair)):
        sair.hide()
        sairblue.draw()
        if (mouse.is_button_pressed(1)):
            break
    else:
        sair.unhide()

    nave.draw()
    logo.draw()
    jogar.draw()
    rank.draw()
    sair.draw()
    janela.update()

