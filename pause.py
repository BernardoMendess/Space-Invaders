from PPlay.window import *
from PPlay.sprite import *


janela = Window(1920,1080)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()

def pause():
    velx = 400
    nave = Sprite("images/nave.png")
    nave.x = 0
    nave.y = 300

    pausar = Sprite("images/pause.png")
    pausar.x = janela.width / 2 - pausar.width / 2
    pausar.y = janela.height / 10

    voltar = Sprite("buttons/voltar.png")
    voltar.x = janela.width / 2 - voltar.width / 2
    voltar.y = janela.height / 1.32 - 150

    voltarblue = Sprite("buttons/voltarblue.png")
    voltarblue.x = janela.width / 2 - voltarblue.width / 2
    voltarblue.y = janela.height / 1.32 - 150

    sair = Sprite("buttons/sair.png")
    sair.x = janela.width / 2 - sair.width / 2
    sair.y = janela.height / 1.21 - 150

    sairblue = Sprite("buttons/sairblue.png")
    sairblue.x = janela.width / 2 - sairblue.width / 2
    sairblue.y = janela.height / 1.21 - 150
    while True:
        janela.set_background_color((0,0,0))
        nave.x += velx * janela.delta_time()
        if nave.x >= janela.width:
            nave.x = -nave.width

        if (mouse.is_over_object(voltar)):
            voltar.hide()
            voltarblue.draw()
            if (mouse.is_button_pressed(1)):
                return False
        else:
            voltar.unhide()

        if (mouse.is_over_object(sair)):
            sair.hide()
            sairblue.draw()
            if (mouse.is_button_pressed(1)):
                return True
        else:
            sair.unhide()

        pausar.draw()
        voltar.draw()
        sair.draw()
        nave.draw()
        janela.update()