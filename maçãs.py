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
    print("-" * 220)
    print("As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. "
          "Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.")
    print("-" * 220)

    condicao = False
    print("Quantas maçãs você comprou?")

    while not condicao:
        macas = input()
        if is_int(macas):
            macas = int(macas)
            condicao = True
        else:
            print("Por favor, digite um número válido.")

    if macas >= 12:
        total = macas
    else:
        total = 1.3 * macas

    print("Você terá que pagar %.2f reais por %d maçãs." % (total, macas))
