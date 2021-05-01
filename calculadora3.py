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


def verificador(texto, real=True):
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


def menu(resultado):
    print("-"*15)
    print("Calculadora")
    print("-"*15)
    print("\nX - Fechar")
    print("C - Clear")
    print("%.2f - Leitor" % resultado)
    print("+ - Soma")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    print("Aperte um número ou uma operação.")
    operacao(resultado)


def operacao(resultado):
    condicao = False
    while not condicao:
        opcao = input()
        if is_float(opcao):
            resultado = float(opcao)
            menu(resultado)
        elif opcao in "+-*/":
            b = verificador("Digite um número.")
            while b == 0 and opcao == "/":
                print("Divisão não permitida.")
                b = verificador("Digite outro número.")
            if opcao == "+":
                resultado = resultado + b
            elif opcao == "-":
                resultado = resultado - b
            elif opcao == "*":
                resultado = resultado * b
            elif opcao == "/":
                resultado = resultado / b
            menu(resultado)
        elif opcao in "Cc":
            resultado = 0
            menu(resultado)
        elif opcao in "Xx":
            opcao = "OFF"
            a.set_status(opcao)
            exit()
        else:
            print("Digite uma opção válida.")


if __name__ == '__main__':
    a = (Calculadora(""))
    while a.get_status() != "ON" and a.get_status() != "OFF":
        print("Aperte ON para ligar a calculadora ou OFF para desligá-la.")
        a.set_status(input())
    if a.get_status() == "ON":
        resultado = 0
        menu(resultado)

