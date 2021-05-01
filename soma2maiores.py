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
    print("-" * 50)
    print("Ler 3 valores e escrever a soma dos dois maiores.")
    print("-" * 50)

    condicao = False
    print("Digite um número!")

    while not condicao:
        a = input()
        if is_float(a):
            a = float(a)
            condicao = True
        else:
            print("Por favor, digite um número.")

    print("Digite outro número, diferente do anterior.")

    while condicao:
        b = input()
        if is_float(b):
            b = float(b)
            if b == a:
                print("Por favor, digite sempre números diferentes.")
            else:
                condicao = False
                if b > a:
                    maior1 = b
                else:
                    maior1 = a

    print("Digite o terceiro e último número!")

    while not condicao:
        c = input()
        if is_float(c):
            c = float(c)
            if c == a or c == b:
                print("Por favor, digite sempre números diferentes.")
            else:
                condicao = True
                if c > b or c > a:
                    maior2 = c
                elif a != maior1:
                    maior2 = a
                else:
                    maior2 = b

    soma = maior1 + maior2

    print("O resultado da soma dos 2 maiores números inseridos é igual a %.2f" % soma)
