from PPlay.window import *
from PPlay.gameimage import *


janela = Window(1920,1080)
teclado = keyboard.Keyboard()
players = []


def adicionar_pontuacao(pontos):
    nome = str(input("Digite seu nick: "))
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(nome + ',' + str(pontos) + '\n')
        arquivo.close()
    return


def sort():
    for i in range(len(players)):
        for j in range(i, len(players)):
            if int(players[j][1]) > int(players[i][1]):
                temp = players[i][0]
                temp2 = players[i][1]
                players[i][0] = players[j][0]
                players[i][1] = players[j][1]
                players[j][0] = temp
                players[j][1] = temp2


def tela_ranking():
    fundo = GameImage("back.jpg")
    with open('ranking.txt', 'r') as arquivo:
        l = arquivo.readlines()
        for linha in l:
            a = linha.rstrip('\n').split(',')
            players.append(a)
    sort()
    while True:
        fundo.draw()
        if (teclado.key_pressed("ESC")):
            break
        if len(players) < 5:
            for i in range(len(players)):
                janela.draw_text(players[i][0], janela.width/3, 150*(i+1), size=125, color=(5, 120, 250))
                janela.draw_text(players[i][1], janela.width / 1.8, 150 * (i + 1), size=125, color=(5, 120, 250))
        elif len(players) >= 5:
            for i in range(5):
                janela.draw_text(players[i][0], janela.width/3, 150*(i+1), size=125, color=(5, 120, 250))
                janela.draw_text(players[i][1], janela.width / 1.8, 150 * (i + 1), size=125, color=(5, 120, 250))

        janela.update()
