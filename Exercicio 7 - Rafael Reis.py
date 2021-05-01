from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *

root = Tk()
root.withdraw()

class Personagem:

    def __init__(self, nome, carro, forca, habilidade, vida):

        self.__nome = nome
        self. __carro = carro
        self. __forca = forca
        self. __habilidade = habilidade
        self. __vida = vida

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def atacar(self):
        if not self.__habilidade or self.__vida == 0:
            return 0
        else:
            return self.__forca

    def defender(self, dano):
        if not self.__habilidade:
            return self.__sofrer_dano(dano)
        elif dano > self.__forca:
            dano = dano - self.__forca
            return self.__sofrer_dano(dano)
        else:
            return self.__sofrer_dano(0)

    def __sofrer_dano(self, dano):
        if dano < self.__vida:
            self.__vida = self.__vida - dano
        else:
            self.__vida = 0

def escolha():
    confirmar = ""

    personagens = dict()
    personagens["Sonic"] = {"Nome": "Sonic", "Carro": "Kart Azul", "Força": 80, "Habilidade": True, "Vida": 50}
    personagens["Mario"] = {"Nome": "Mario", "Carro": "Kart Vermelho", "Força": 50, "Habilidade": None, "Vida": 80}
    personagens["Luigi"] = {"Nome": "Luigi", "Carro": "Kart Verde", "Força": 30, "Habilidade": None, "Vida": 100}
    personagens["Pikachu"] = {"Nome": "Pikachu", "Carro": "Kart Amarelo", "Força": 70, "Habilidade": True, "Vida": 20}

    while confirmar != "SIM":
        print("\nEscolha um personagem entre os seguintes:")
        for i in personagens:
            print(i)
        print("Digite o nome do personagem:")
        escolha = input()
        print(personagens[escolha])
        print("Digite sim para confirmar a escolha, ou qualquer outra coisa para escolher novamente.")
        confirmar = input().upper()

    print(personagens)
    return escolha

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Bem vindo ao jogo!")

    escolha = escolha()

    if escolha == "Sonic":
        p1 = Personagem("Sonic", "Azul", 80, True, 50)
        p2 = Personagem("Mario", "Vermelho", 50, False, 80)
        p3 = Personagem("Luigi", "Verde", 30, False, 100)
        p4 = Personagem("Pikachu", "Amarelo", 70, True, 20)
    elif escolha == "Mario":
        p2 = Personagem("Sonic", "Azul", 80, True, 50)
        p1 = Personagem("Mario", "Vermelho", 50, None, 80)
        p3 = Personagem("Luigi", "Verde", 30, None, 100)
        p4 = Personagem("Pikachu", "Amarelo", 70, True, 20)
    elif escolha == "Luigi":
        p3 = Personagem("Sonic", "Azul", 80, True, 50)
        p2 = Personagem("Mario", "Vermelho", 50, None, 80)
        p1 = Personagem("Luigi", "Verde", 30, None, 100)
        p4 = Personagem("Pikachu", "Amarelo", 70, True, 20)
    elif escolha == "Pikachu":
        p4 = Personagem("Sonic", "Azul", 80, True, 50)
        p2 = Personagem("Mario", "Vermelho", 50, None, 80)
        p3 = Personagem("Luigi", "Verde", 30, None, 100)
        p1 = Personagem("Pikachu", "Amarelo", 70, True, 20)

    print("Seu personagem é o", p1.get_nome(), ".")

    print("Deseja atacar", p2.get_nome(), "? S/N")
    ataque = input().upper()

    if ataque == "S":
        p2.defender(p1.atacar())
        print("Vida restante de", p2.get_nome(), ":", p2.get_vida())
    else:
        print("Deseja atacar", p3.get_nome(), "? S/N")
        ataque = input().upper()
        if ataque == "S":
            p3.defender(p1.atacar())
        else:
            print("Você então atacará", p4.get_nome(), ".")
            p4.defender(p1.atacar())



