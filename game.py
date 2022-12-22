from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
from pause import pause
from ranking import tela_ranking
import random


janela = Window(1920,1080)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
tiros = []
monstros = []
vidas = []
tiro_alien = []
pontos = [0]

nave = Sprite("images/nave2.png")

perd = Sprite("images/perdeu.png")
perd.set_position((janela.width - perd.width)/2, (janela.height - perd.height)/2)


def gerar_vidas():
    for i in range(3):
        vida = Sprite("images/vida.png")
        vida.set_position(i*10 + (i+1)*vida.width, janela.height - vida.height -10)
        vidas.append(vida)


def desenhar_vidas():
    for vida in vidas:
        vida.draw()


def atirar():
    tiro = Sprite("images/tiro.png")
    tiro.set_position(nave.x + nave.width/2, nave.y)
    tiros.append(tiro)


def desenhar_tiros():
    vely = -450
    for tiro in tiros:
        tiro.y += vely * janela.delta_time()
        tiro.draw()
    for tiro in tiros:
        if tiro.y < 0:
            tiros.remove(tiro)


def checar_linha():
    for linha in monstros:
        if(len(linha) == 0):
            monstros.remove(linha)


def matriz_monstros(xl, yl):
    for i in range(xl):
        linha = []
        for j in range(yl):
            monstro = Sprite("images/alien1.png", 2)
            monstro.set_total_duration(1000)
            monstro.x = 20 + i * monstro.width * 1.5
            monstro.y = 20 + j * monstro.height * 1.5
            linha.append(monstro)
        monstros.append(linha)


def acertou_monstro(pi_x, pi_y, pf_x, pf_y, monstro_w, monstro_h):
    for tiro in tiros:
        if tiro.x >= pi_x and tiro.y >= pi_y:
            if tiro.x <= pi_x + pf_x + monstro_w and tiro.y <= pi_y + pf_y + monstro_h:
                for linha in monstros:
                    for monstro in linha:
                        if(tiro.collided(monstro)):
                            tiros.remove(tiro)
                            linha.remove(monstro)
                            return True

def limpa_matriz():
    for linha in monstros:
        for monstro in linha:
            linha.remove(monstro)
        monstros.remove(linha)


def desenha_monstros():
    for linha in monstros:
        for monstro in linha:
            monstro.draw()
            monstro.update()


def tiro_aliens(alvivos):
    x = random.randint(0, alvivos)
    cont = 0
    tiroal = Sprite("images/tiroalien.png")
    for linha in monstros:
        for monstro in linha:
            if x == cont:
                tiroal.set_position(monstro.x + monstro.width / 2, monstro.y)
                tiro_alien.append(tiroal)
            cont += 1


def desenhar_tirosal():
    vely = 450
    for tiro in tiro_alien:
        tiro.y += vely * janela.delta_time()
        tiro.draw()
    for tiro in tiro_alien:
        if tiro.y > janela.height:
            tiro_alien.remove(tiro)


def checar_dano():
    for tiro in tiro_alien:
        if tiro.collided(nave):
            vidas.pop(len(vidas)-1)
            tiro_alien.remove(tiro)
            return True


def checar_posicao():
    for linha in monstros:
        for monstro in linha:
            if monstro.y + monstro.height >= nave.y:
                return True


def checar_tiros():
    for tiro in tiros:
        for tiro_al in tiro_alien:
            if tiro.collided(tiro_al):
                tiros.remove(tiro)
                tiro_alien.remove(tiro_al)
                break


def jogo():
    FPS = 0
    cont = 0
    velmonstro = 75
    velnave = 400
    aum_pont = 0
    bateu_r = False
    bateu_l = False
    bt = 0
    perdeu = False
    tempo_pontos = 0
    temp_trocartela = 0
    tempo_recarga_player = 0
    tempo_fps = 0
    tempo_recarga_alien = 0
    tempo_espera = 0
    tempo_inv = 0
    contador_espera = 0
    levar_tiro = True
    c_inv = 0
    pode_atirar = 0
    inicio = 0
    b = 0
    xl = 10
    yl = 6
    alvivos = 0
    monstro_w = 0
    monstro_h = 0
    pf_x = 0
    pf_y = 0
    pi_x = 0
    pi_y = 0
    muda_numero_fase = 0
    fase = 0
    nave.x = (janela.width - nave.width) / 2
    nave.y = janela.height - nave.height * 3
    gerar_vidas()
    while True:
        janela.set_background_color((0, 0, 0))
        #fazendo o player piscar antes de os aliens serem desenhados
        if alvivos == 0 and perdeu == False:
            tempo_espera += 1
            pode_atirar = 1
            if muda_numero_fase == 0:
                fase += 1
                muda_numero_fase += 1
            texto = 'Fase ' + str(fase)
            janela.draw_text(texto, (janela.width/2) - 150, (janela.height/2) - 100, size=100, color=(5, 120, 250))

            if tempo_espera == 100:
                nave.hide()
            elif tempo_espera == 150:
                nave.unhide()
                contador_espera += 1
                tempo_espera = 0

            #gerando a matriz de monstros
            if contador_espera == 5:
                pontos[0] += 100 * aum_pont
                alvivos = xl * yl
                matriz_monstros(xl, yl)
                monstro_w = monstros[0][0].width
                monstro_h = monstros[0][0].height
                pf_x = monstros[-1][-1].x
                pf_y = monstros[-1][-1].y
                pi_x = monstros[0][0].x
                pi_y = monstros[0][0].y
                velmonstro *= 1.4
                velnave *= 1.1
                aum_pont += 1
                inicio = 1
                contador_espera = 0
                muda_numero_fase = 0
                pode_atirar = 0

        if (teclado.key_pressed("ESC")):
            if(pause()):
                break

        #verificando se o jogador ainda possui vidas
        if(len(vidas) == 0):
            perdeu = True

        #verificando se a posição dos monstros é maior que a posição do jogador
        if (checar_posicao()):
            perdeu = True

        #movimentação dos monstros
        for linha in monstros:
            for monstro in linha:
                monstro.x += velmonstro * janela.delta_time()

                if monstro.x <= 0:
                    bateu_r = True
                    velmonstro *= -1
                    for linha in monstros:
                        for monstro in linha:
                            monstro.x += 1

                if monstro.x >= janela.width - monstro.width:
                    velmonstro *= -1
                    bateu_l = True
                    for linha in monstros:
                        for monstro in linha:
                            monstro.x -= 1

                if bateu_r == True or bateu_l == True:
                    for linha in monstros:
                        for monstro in linha:
                            monstro.y += janela.height//20
                    bateu_l = False
                    bateu_r = False
                    bt = 1

        pi_x += velmonstro * janela.delta_time()
        if bateu_r == True:
            pi_x += 1
        if bateu_l == True:
            pi_x -= 1
        if bt == 1:
            pi_y += janela.height // 20
            bt = 0

        #movimentação da nave
        if nave.x >= 0:
            if (teclado.key_pressed("LEFT")):
                nave.x -= velnave * janela.delta_time()

        if nave.x <= janela.width - nave.width:
            if (teclado.key_pressed("RIGHT")):
                nave.x += velnave * janela.delta_time()

        #tiro do player
        if tempo_recarga_player == 0 and pode_atirar == 0:
            if(teclado.key_pressed("SPACE")):
                atirar()
                tempo_recarga_player += 1

        #sistema de recarga do tiro do player
        if tempo_recarga_player != 0:
            tempo_recarga_player += 1
            if tempo_recarga_player >= 150:
                tempo_recarga_player = 0

        #tempo de recarga do tiro dos aliens
        tempo_recarga_alien += 1
        if tempo_recarga_alien >= 350:
            tiro_aliens(alvivos)
            tempo_recarga_alien = 0

        #Sistema de pontuação
        tempo_pontos += 2
        if (acertou_monstro(pi_x, pi_y, pf_x, pf_y, monstro_w, monstro_h)):
            alvivos -= 1
            pontos[0] += 10
        checar_linha()

        txt = "Pontuação: " + str(pontos[0])

        #checando se o player levou um tiro e resetando a posição dele
        if levar_tiro == True:
            if(checar_dano() == True):
                pode_atirar = 1
                b = 1
                pontos[0] -= 100

        if pontos[0] < 0:
            pontos[0] = 0

        if b == 1:
            levar_tiro = False
            nave.set_position((janela.width - nave.width) / 2,  janela.height - nave.height * 3)
            if c_inv == 2:
                b = 0

        if pode_atirar == 0:
            levar_tiro = True

        if levar_tiro == False:
            if c_inv < 5:
                tempo_inv += 1
                if tempo_inv == 100:
                    nave.hide()
                if tempo_inv == 150:
                    nave.unhide()
                    tempo_inv = 0
                    c_inv += 1
            else:
                c_inv = 0
                pode_atirar = 0

        checar_tiros()

        #frame rate do jogo
        tempo_fps += janela.delta_time()
        cont += 1
        if tempo_fps >= 1:
            tempo_fps = 0
            FPS = cont
            cont = 0

        #procedimentos após o jogador perder
        if perdeu == True:
            limpa_matriz()
            perd.draw()
            alvivos = 0
            inicio = 0

        if perdeu == True:
            temp_trocartela += 1
            if temp_trocartela == 500:
                tela_ranking(pontos)
                break

        janela.draw_text(txt, janela.width - 240, janela. height - 60, size=25, color=(5, 120, 250))
        janela.draw_text(str(FPS), 10, 10, size=25, color=(5, 120, 250))
        desenhar_tiros()
        desenhar_vidas()
        desenhar_tirosal()
        nave.draw()
        desenha_monstros()
        janela.update()