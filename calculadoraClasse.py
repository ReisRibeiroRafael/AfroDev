from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import math
from Calculadora import Calculadora
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


def verificadornumero(texto, real=True):
    validador = False
    while not validador:
        print(texto)
        entrada = input()
        if real:
            if is_float(entrada):
                return float(entrada)
            else:
                print("Erro! Digite um número válido.")
        else:
            if is_int(entrada):
                return int(entrada)
            else:
                print("Erro! Digite um número válido.")


def verificadoropcao(texto):
    validador = False
    while not validador:
        print(texto)
        entrada = input()
        if entrada in "+*-/CcXx":
            return entrada
        else:
            print("Digite uma opção válida!")


if __name__ == '__main__':
    a = (Calculadora(""))
    resultado = 0

    print("Aperte ON para ligar a calculadora ou OFF para desligá-la.")

    while a.get_status() != "ON" and a.get_status() != "OFF":
        a.set_status(input())

    if a.get_status() == "ON":
        while a.get_status() != "OFF":
            print("-" * 15)
            print("Calculadora")
            print("-" * 15)
            print("\nX - Fechar")
            print("C - Clear")
            print("%.2f - Leitor" % resultado)
            print("+ - Soma")
            print("- - Subtração")
            print("* - Multiplicação")
            print("/ - Divisão")
            num2 = 0

            print("Digite um número ou uma operação.")
            num1 = input().upper()
            if not is_float(num1):
                opcao = num1
                if opcao == "X":
                    a.set_status("OFF")
                elif opcao == "C":
                    a.operacao("C", 1, 1)
            else:
                num1 = float(num1)
                opcao = verificadoropcao("Digite uma operação.")
                if opcao in "Xx":
                    a.set_status("OFF")
                elif opcao in "Cc":
                    resultado = a.operacao(opcao, 1, 1)
                else:
                    num2 = verificadornumero("Digite outro número!")
                    while opcao == "/" and num2 == 0:
                        print("Não existe divisão por 0.")
                        num2 = verificadornumero("Digite outro número!")

                resultado = a.operacao(opcao, num1, num2)

