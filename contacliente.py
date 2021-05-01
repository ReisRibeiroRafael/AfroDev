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
    print("-" * 300)
    print("Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever "
          "o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou "
          "igual a zero escrever a mensagem 'Saldo Positivo, senão escrever a mensagem 'Saldo Negativo'.")
    print("-" * 300)

    condicao = False
    print("Digite o número da conta do cliente.")

    while not condicao:
        conta = input()
        if is_int(conta):
            condicao = True
        else:
            print("Por favor, digite o número da conta do cliente.")

    print("Digite o saldo da conta", conta)

    while condicao:
        saldo = input()
        if is_float(saldo):
            saldo = float(saldo)
            if saldo >= 0:
                condicao = False
            else:
                print("Digite um número válido para o saldo.")
        else:
            print("Digite um número válido para o saldo.")

    print("Digite o debito da conta", conta)

    while not condicao:
        debito = input()
        if is_float(debito):
            debito = float(debito)
            if debito >= 0:
                condicao = True
            else:
                print("Digite um número válido para o débito.")
        else:
            print("Digite um número válido para o débito.")

    print("Digite o credito da conta", conta)

    while condicao:
        credito = input()
        if is_float(credito):
            credito = float(credito)
            if credito >= 0:
                condicao = False
            else:
                print("Digite um número válido para o credito.")
        else:
            print("Digite um número válido para o credito.")

    atual = saldo - debito + credito

    if atual >= 0:
        print("\nSaldo é %.2f reais. Saldo positivo!" % atual)
    else:
        print("\nSaldo é %.2f reais. Saldo negativo." % atual)





