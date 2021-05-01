from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import math

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


def menu():
    print("-" * 30)
    print("Calculadora")
    print("-" * 30)
    print("Opções da calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do programa.\n")
    opcao = verificador("Qual opção você deseja selecionar?", False)
    return opcao


if __name__ == '__main__':
    fim = False

    while not fim:
        opcao = menu()
        if (opcao == 1) or (opcao == 2) or (opcao == 3) or (opcao == 4):
            a = verificador("Digite o primeiro número!")
            b = verificador("Digite o segundo número!")
            while opcao == 4 and b == 0:
                print("Você não pode dividir por 0. Não quebre a matemática.")
                b = verificador("Digite o segundo número!")
            else:
                if opcao == 1:
                    resultado = a + b
                elif opcao == 2:
                    resultado = a - b
                elif opcao == 3:
                    resultado = a * b
                elif opcao == 4:
                    resultado = a / b
                print("Resultado da sua operação é igual a %.2f" % resultado)
                print("Aperte enter para continuar")
                input()
        elif (opcao == 5):
            print("Fim do programa!")
            fim = True
        else:
            print("Opção inválida! Aperte enter para exibir o menu novamente!")
            input()
