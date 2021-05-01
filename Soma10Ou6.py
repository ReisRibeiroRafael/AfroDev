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
    print("-" * 75)
    print("Some dois números e divida por 2 se a soma for maior que 10 ou igual a 6.")
    print("-" * 75)

    condicao = False
    print("Digite um numero!")

    while not condicao:
        a = input()
        if is_int(a):
            a = int(a)
            condicao = True
        else:
            print("Por favor, digite um número válido.")

    print("Digite outro número!")
    while condicao:
        b = input()
        if is_int(b):
            b = int(b)
            condicao = False
        else:
            print("Por favor, digite um número válido.")

    if (a + b > 10) | (a + b == 6):
        resultado = (a + b) / 2
        print("O valor de sua soma é %d. Este número dividido por 2 é igual a: %.1f." % (resultado * 2, resultado))
    else:
        resultado = a + b
        print("O valor de sua soma é %d. Se fosse maior que 10 ou igual a 6, a dividiríamos por 2." % resultado)

        (((((((())))))))
