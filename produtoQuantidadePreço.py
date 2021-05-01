from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *

root = Tk()
root.withdraw()


def is_float(valor):
    try:
        float(valor)
    except:
        return False

    return True


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


if __name__ == '__main__':
    print("-" * 105)
    print("Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário.")
    print("-" * 105)

    condicao = False
    print("Digite o nome do produto.")

    while not condicao:
        nome = input().title()
        if is_float(nome):
            print("Por favor, digite um nome válido.")
        else:
            condicao = True

    print("Digite a quantidade comprada do produto", nome)

    while condicao:
        quantidade = input()
        if is_int(quantidade):
            quantidade = int(quantidade)
            if quantidade >= 0:
                condicao = False
            else:
                print("Por favor, digite uma quantidade maior ou igual a zero.")
        else:
            print("Por favor, digite uma quantidade maior ou igual a zero.")

    print("Digite o preço unitário, em reais, do produto", nome)

    while not condicao:
        preco = input()
        if is_float(preco):
            preco = float(preco)
            if preco >= 0:
                condicao = True
            else:
                print("Por favor, digite um preço válido.")
        else:
            print("Por favor, digite um preço válido.")

    if quantidade <= 5:
        desconto = 0.02
    elif quantidade > 10:
        desconto = 0.05
    else:
        desconto = 0.03

    total = quantidade * preco
    totalpago = total * (1 - desconto)

    print("Você pagaria %.2f, mas graças ao desconto de %d%%, você pagará %.2f!" % (total, desconto*100, totalpago))



