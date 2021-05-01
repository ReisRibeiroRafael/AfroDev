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
    print("Área do retângulo e verificar se é triângulo.")
    print("-" * 50)

    # #Retângulo
    condicao = False
    print("Digite o valor da base do seu retângulo.")

    while not condicao:
        b = input()

        if is_float(b):
            b = float(b)
            if b > 0:
                condicao = True
            else:
                print("Por favor, digite um número maior que 0.")
        else:
            print("Por favor, digite um número maior que 0.")

    print("Digite o valor da altura do seu retângulo.")

    while condicao:
        h = input()

        if is_float(h):
            h = float(h)
            if h > 0:
                condicao = False
            else:
                print("Por favor, digite um número maior que 0.")
        else:
            print("Por favor, digite um número maior que 0.")

    area = b * h
    print("Seu retângulo tem área %.2f u.a" % area)

    # Triângulo
    # condicao = False
    #
    # print("Digite o valor de um lado do seu triângulo.")
    #
    # while not condicao:
    #     A = input()
    #     if is_float(A):
    #         A = float(A)
    #         if A > 0:
    #             condicao = True
    #         else:
    #             print("Por favor, digite um número maior que 0.")
    #     else:
    #         print("Por favor, digite um número maior que 0.")
    #
    # print("\nDigite o valor de outro lado do seu triângulo.")
    #
    # while condicao:
    #     B = input()
    #     if is_float(B):
    #         B = float(B)
    #         if B > 0:
    #             condicao = False
    #         else:
    #             print("Por favor, digite um número maior que 0.")
    #     else:
    #         print("Por favor, digite um número maior que 0.")
    #
    # print("\nDigite o valor de outro lado do seu triângulo.")
    #
    # while not condicao:
    #     C = input()
    #     if is_float(C):
    #         C = float(C)
    #         if C > 0:
    #             condicao = True
    #         else:
    #             print("Por favor, digite um número maior que 0.")
    #     else:
    #         print("Por favor, digite um número maior que 0.")
    #
    # if C >= A + B or B >= A + C or A >= B + C:
    #     print("\n%.1f, %.1f e %.1f não formam um triângulo." % (A, B, C))
    # else:
    #     print("\n%.1f, %.1f e %.1f formam um triângulo." % (A, B, C))
