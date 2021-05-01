from tkinter import messagebox
from tkinter import simpledialog
from tkinter import*

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
    print("-"*70)
    print("Faça um algoritmo para verificar se o número é maior que 10 e par.")
    print("-"*70)

    condicao = False
    print("Digite um número inteiro!")

    while not condicao:
        a = input()

        if not is_int(a):
            print("Por favor, digite um número inteiro!")
        else:
            a = int(a)
            condicao = True

    if (a % 2) == 0:
        par = True
    else:
        par = False

    if a > 10:
        if par:
            print("%d é maior que 10 e é par." % (a))
        else:
            print("%d é maior que 10 e é ímpar." %(a))
    else:
        if par:
            print("%d é menor que 10 e é par." %(a))
        else:
            print("%d é menor que 10 e é ímpar." %(a))