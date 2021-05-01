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
    print("Nota, número de faltas e aprovação do aluno.")
    print("-" * 50)

    condicao = False
    print("Digite a nota do aluno.")

    while not condicao:
        nota = input()

        if is_float(nota):
            nota = float(nota)
            if (nota >= 0) and (nota <= 10):
                condicao = True
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        else:
            print("Por favor, digite uma nota numérica.")

    print("Digite o número de faltas do aluno.")

    while condicao:
        falta = input()

        if is_float(falta):
            falta = float(falta)
            if falta >= 0:
                condicao = False
            else:
                print("Por favor, digite um número de faltas maior ou igual a 0.")
        else:
            print("Por favor, digite um número.")

    if nota == 10:
        print("\nAprovado com mérito!")
    elif (nota >= 8) and (nota < 10) and (falta < 15):
        print("\nAprovado!")
    elif (nota >= 6) and (nota < 8) and (falta < 10):
        print("\nAprovado com restrição.")
    else:
        print("\nReprovado...")
