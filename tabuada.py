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
    print("-" * 10)
    print("Tabuada de um número")
    print("-" * 10)

    condicao = False
    contador = 1
    print("Digite um número para saber a tabuada deste.")

    while not condicao:
        a = input()
        if is_int(a):
            a = int(a)
            if a > 0:
                condicao = True
            else:
                print("Digite um número inteiro maior que 0.")
        else:
            print("Digite um número inteiro maior que 0.")

    while contador != 11:
        resultado = a * contador
        print("%d * %d = %d" % (a, contador, resultado))
        contador = contador + 1
