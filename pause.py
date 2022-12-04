from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *

janela = Window(1920,1080)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()

def pause():
    velx = 400
    nave = Sprite("nave.png")
    nave.x = 0
    nave.y = 300

    pausar = Sprite("pause.png")
    pausar.x = janela.width / 2 - pausar.width / 2
    pausar.y = janela.height / 10

    voltar = Sprite("voltar.png")
    voltar.x = janela.width / 2 - voltar.width / 2
    voltar.y = janela.height / 1.32

    voltarblue = Sprite("voltarblue.png")
    voltarblue.x = janela.width / 2 - voltarblue.width / 2
    voltarblue.y = janela.height / 1.32

    sair = Sprite("sair.png")
    sair.x = janela.width / 2 - sair.width / 2
    sair.y = janela.height / 1.21

    sairblue = Sprite("sairblue.png")
    sairblue.x = janela.width / 2 - sairblue.width / 2
    sairblue.y = janela.height / 1.21
    while True:
        janela.set_background_color((0,0,0))
        nave.x += velx * janela.delta_time()
        if nave.x >= janela.width:
            nave.x = -nave.width

        if (mouse.is_over_object(voltar)):
            voltar.hide()
            voltarblue.draw()
            if (mouse.is_button_pressed(1)):
                break
        else:
            voltar.unhide()

        if (mouse.is_over_object(sair)):
            sair.hide()
            sairblue.draw()
            if (mouse.is_button_pressed(1)):
                janela.close()
        else:
            sair.unhide()

        pausar.draw()
        voltar.draw()
        sair.draw()
        nave.draw()
        janela.update()