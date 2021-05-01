from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import math

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


def inicio():
    print("-" * 30)
    print("Calculadora de 2 números.")
    print("-" * 30 + "\n")


def menu(a, b):
    print("\n")
    print("Digite um número de acordo com a operação desejada.")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = input()

    try:
        is_int(opcao)
    except:
        print("Por favor, escolha uma opção válida.")
    else:
        if opcao == '1':
            resultado = a + b
            return resultado
        elif opcao == '2':
            resultado = a - b
            return resultado
        elif opcao == '3':
            resultado = a * b
            return resultado
        elif opcao == '4':
            if b != 0:
                resultado = a / b
                return resultado
            else:
                print("Não faça divisão por 0. Vamos recomeçar. \n")
                resultado = False
        else:
            print("Por favor, escolha uma opção válida.")


if __name__ == '__main__':
    inicio()
    resultado = False
    condicao = False

    while not condicao:
        print("Digite o primeiro número da operação:")
        a = input()
        print("Digite o segundo número da operação:")
        b = input()
        if is_float(a) and is_float(b):
            a = float(a)
            b = float(b)
            resultado = menu(a, b)
            if resultado:
                print("O resultado da sua operação é igual a: %.2f" % resultado)
                print("Digite 1 se deseja parar o programa.")
                opcao = input()
                if opcao == '1':
                    condicao = True
        else:
            print("Digite números válidos!")
