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
    print("-" * 80)
    print("Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.")
    print("-" * 80)

    soma = 0
    contador = 1
    condicao = False

    while contador != 11:
        print("Digite o %d° valor para calcular a sua média." % contador)
        while not condicao:
            a = input()
            if is_float(a):
                a = float(a)
                soma = soma + a
                condicao = True
            else:
                print("Por favor, digite um número válido.")
        contador = contador + 1
        condicao = False

    media = soma/10

    print("O valor de sua média é igual a: %.2f" % (media))
