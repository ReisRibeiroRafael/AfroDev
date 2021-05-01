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


if __name__ == '__main__':
    print("-"*165)
    print("Faça um programa que leia o nome do aluno e sua respective nota (número indeterminado de alunos)."
          "Mostre na tela o nome do aluno que tirou a maior e a menor nota.")
    print("-"*165)

    dicionario = dict()


