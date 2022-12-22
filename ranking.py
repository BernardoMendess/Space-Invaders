from PPlay.window import *
from PPlay.sprite import *


janela = Window(1920,1080)
teclado = keyboard.Keyboard()
mouse = mouse.Mouse()
players = []

qt = Sprite("buttons/sair.png")
qt.set_position(janela.width - qt.width - 50, janela.height - qt.height - 50)

qtred = Sprite("buttons/sairblue.png")
qtred.x = janela.width/2 - qtred.width/2.3
qtred.y = janela.height/1.25
qtred.set_position(janela.width - qtred.width - 50, janela.height - qtred.height - 50)


def sort(player):
    for ind in range(len(player)):
        min_index = ind
        for j in range(ind + 1, len(player)):
            if int(player[j].split(' ')[1]) <= int(player[min_index].split(' ')[1]):
                min_index = j
        (player[ind], player[min_index]) = (player[min_index], player[ind])
    player.reverse()


def tela_ranking(point):
    player = []
    if point[0] >= 0:
        a = ["_", "_", "_"]
        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        b = 0
        c = 0
        ct = 0
        cc = 0

        while True:

            janela.set_background_color((0, 0, 0))

            for i in range(3):
                if (teclado.key_pressed("UP") and ct == 0):
                    ct += 1
                    if c == 26:
                        c = 0
                    a[b] = alfabeto[c]
                    c = c + 1

                if (teclado.key_pressed("DOWN") and ct == 0):
                    ct += 1
                    c = c - 1
                    if c == -1:
                        c = 25
                    a[b] = alfabeto[c]

                if (teclado.key_pressed("ENTER") and cc == 0 and a[b] != "_"):
                    cc += 1
                    c = 0
                    b += 1

                if ct != 0:
                    ct += 1
                    if ct == 100:
                        ct = 0

                if cc != 0:
                    cc += 1
                    if cc == 100:
                        cc = 0
                janela.draw_text(a[i], janela.width / 2 - 140 + 70 * i + 1, 130, size=100, color=(255, 255, 255))

            if b == 3:
                player.append(a[0] + a[1] + a[2] + " " + str(point[0]))
                break
            janela.update()

    with open('ranking.txt', 'r') as arquivo:
        l = arquivo.readlines()
        for linha in l:
            a = linha.rstrip('\n')
            player.append(a)
        arquivo.close()

    sort(player)

    arq = open("ranking.txt", "w")
    for lnh in player:
        arq.write(lnh)
        arq.write("\n")
    arq.close()

    while True:
        janela.set_background_color((0, 0, 0))
        for i in range(len(player)):
            if i == 5:
                break
            janela.draw_text(player[i], janela.width / 2 - 140, 50 + 80 * (i + 1), size=75, color=(255, 255, 255))
        if (mouse.is_over_object(qt)):
            qt.hide()
            qtred.draw()
            if (mouse.is_button_pressed(1)):
                return True
        else:
            qt.unhide()
        qt.draw()
        janela.update()