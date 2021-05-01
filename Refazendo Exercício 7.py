from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import random

root = Tk()
root.withdraw()


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


def menupersonagem():
    condicao = False
    while not condicao:
        listapersonagem = dict()
        listapersonagem["Sonic"] = {"Nome: Sonic | Habilidade: Spin Dash | Vida: 200 | Força: 50"}
        listapersonagem["Mario"] = {"Nome: Mario | Habilidade: Fogo | Vida: 150 | Força: 80"}
        listapersonagem["Pikachu"] = {"Nome: Pikachu | Habilidade: Choque do Trovão | Vida: 120 | Força: 100"}

        print("Escolha um personagem da lista:")
        for i in listapersonagem:
            print(listapersonagem[i])

        personagem = input().title()
        condicao = escolhapersonagem(personagem)

    return personagem


def escolhapersonagem(personagem):
    listapersonagem = dict()
    listapersonagem["Sonic"] = {"Nome: Sonic | Habilidade: Spin Dash | Vida: 200 | Força: 50"}
    listapersonagem["Mario"] = {"Nome: Mario | Habilidade: Fogo | Vida: 150 | Força: 80"}
    listapersonagem["Pikachu"] = {"Nome: Pikachu | Habilidade: Choque do Trovão | Vida: 120 | Força: 100"}
    
    for i in listapersonagem:
        if personagem == i:
            return True

    print("Escolha um personagem válido.")
    return False


def criarpersonagem(personagem):
    p1 = Jogo("Sonic", "Spin Dash", 200, 50)
    p2 = Jogo("Mario", "Fogo", 150, 80)
    p3 = Jogo("Pikachu", "Choque do Trovão", 120, 100)

    if personagem == "Sonic":
        jogador1 = p1
        jogador2 = p2
        jogador3 = p3
    if personagem == "Mario":
        jogador1 = p2
        jogador2 = p1
        jogador3 = p3
    if personagem == "Pikachu":
        jogador1 = p3
        jogador2 = p2
        jogador3 = p1

    jogadores = (jogador1, jogador2, jogador3)
    return jogadores


def partida(jogadores):
    while jogadores[0].get_vida() != 0 and jogadores[1].get_vida() != 0 and jogadores[2].get_vida() != 0:
        condicao = False
        while not condicao:
            print(f"\nVocê é o {jogadores[0].get_nome()}. Deseja atacar {jogadores[1].get_nome()} ou {jogadores[2].get_nome()}?")
            atacado = input()
            condicao = escolhapersonagem(atacado)
            if condicao:
                for x in range(0, 3, 1):
                    if jogadores[x].get_nome() == atacado:
                        jogadores[x].defender(jogadores[0].atacar())
                        print(f"{jogadores[0].get_nome()} utiliza {jogadores[0].get_habilidade()} em {jogadores[x].get_nome()}!")
                        print(f"{jogadores[x].get_nome()} sofreu {jogadores[0].get_forca(jogadores[x].atacar())} de dano e possui agora {jogadores[x].get_vida()} de vida.")
                        input("Digite qualquer tecla para continuar.")

        x = random.choice([0, 2])
        jogadores[x].defender(jogadores[1].atacar())
        print(f"\n{jogadores[1].get_nome()} utiliza {jogadores[1].get_habilidade()} em {jogadores[x].get_nome()}!")
        print(
            f"{jogadores[x].get_nome()} sofreu {jogadores[1].get_forca(jogadores[x].atacar())} de dano e possui agora {jogadores[x].get_vida()} de vida.")
        input("Digite qualquer tecla para continuar.")

        x = random.choice([0, 1])
        jogadores[x].defender(jogadores[2].atacar())
        print(f"\n{jogadores[2].get_nome()} utiliza {jogadores[2].get_habilidade()} em {jogadores[x].get_nome()}!")
        print(
            f"{jogadores[x].get_nome()} sofreu {jogadores[2].get_forca(jogadores[x].atacar())} de dano e possui agora {jogadores[x].get_vida()} de vida.")
        input("Digite qualquer tecla para continuar.")

    for x in range(0, 3, 1):
        if jogadores[x].get_vida() == 0:
            print(f"\n{jogadores[x].get_nome()} chegou a 0 de vida e perdeu.")


class Jogo:
    def __init__(self, nome, habilidade, vida, forca):
        self.__nome = nome
        self.habilidade = habilidade
        self.__vida = vida
        self.__forca = forca

    def get_nome(self):
        return self.__nome

    def get_forca(self, defesa):
        dano = abs(self.__forca - defesa)
        return dano

    def get_habilidade(self):
        return self.habilidade

    def get_vida(self):
        return self.__vida

    def defender(self, ataque):
        dano = abs(self.__forca - ataque)
        self.__sofrerdano(dano)

    def atacar(self):
        ataque = self.__forca
        return ataque

    def __sofrerdano(self, dano):
        if dano > self.__vida:
            self.__vida = 0
        else:
            self.__vida = self.__vida - dano


if __name__ == '__main__':
    personagem = menupersonagem()
    jogadores = criarpersonagem(personagem)
    partida(jogadores)