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


def validadornota(texto):
    condicao = False
    print(texto)
    while not condicao:
        nota = input()
        if (is_float(nota)):
            nota = float(nota)
            if (nota >= 0) and (nota <= 10):
                condicao = True
                return nota
            else:
                print("Digite uma nota válida.")
        else:
            print("Digite uma nota válida.")


def media(tamanho):
    soma = 0
    for cont in range(tamanho):
        soma = soma + lista[cont]
    return float(soma)


def validadornome(texto):
    condicao = False
    print(texto)
    while not condicao:
        nome = input()
        if is_float(nome):
            print("Digite um nome válido.")
        else:
            return nome


def dicionario():
    dicionario = dict()
    cont = 1
    fim = False

    while not fim:
        print("Nome e nota do %dª aluno:" % cont)
        nome = validadornome("Digite o nome do aluno.")
        nota = validadornota("Digite a nota de " + nome)
        dicionario[nome] = nota
        cont = cont + 1
        print("Digite sair se deseja encerrar o programa. Se deseja continuar, digite qualquer outra coisa.")
        end = input().upper()
        if end == "SAIR":
            return dicionario


def validadornumero(texto):
    condicao = False
    print(texto)

    while not condicao:
        a = input()
        if is_int(a):
            return a
        else:
            print("Por favor, digite um número inteiro.")



if __name__ == '__main__':
    # EXERCÍCIO 1:
    # print("-"*70)
    # print("Leia um programa que leia 4 notas, mostre as notas e a média na tela.")
    # print("-"*70)
    # lista = []
    #
    # for cont in range(0, 4, 1):
    #     nota = validadornota("Digite a %dª nota" % (cont + 1))
    #     lista.insert(cont, nota)
    #
    # media = media(len(lista))
    #
    # for cont in range (0,len(lista),1):
    #     print("Nota %d: %.2f" % (cont + 1, lista[cont]))
    #
    # print("Media das notas: %.2f" % (media/len(lista)))

    # EXERCÍCIO 2 - ESSE DEU TRABALHO!!:
    # print("-" * 165)
    # print("Faça um programa que leia o nome do aluno e sua respective nota (número indeterminado de alunos)."
    #       "Mostre na tela o nome do aluno que tirou a maior e a menor nota.")
    # print("-" * 165)
    #
    # sistema = dicionario()
    # maior = -1
    # menor = 11
    # alunomaior = []
    # alunomenor = []
    #
    # for nome, nota in sistema.items():
    #     if nota > maior:
    #         alunomaior.clear()
    #         alunomaior.append(nome)
    #         maior = nota
    #     elif nota == maior:
    #         alunomaior.append(nome)
    #     if nota < menor:
    #         alunomenor.clear()
    #         alunomenor.append(nome)
    #         menor = nota
    #     elif nota == menor:
    #         alunomenor.append(nome)
    #
    # print("Aluno(s) de maior nota: ", alunomaior, ". Nota %.1f" % maior)
    # print("Aluno(s) de menor nota: ", alunomenor, ". Nota %.1f" % menor)



    # EXERCÍCIO 3 - Só consegui fazer no limite do tempo, não deu para otimizar
    print("-" * 70)
    print("Faça um programa que remova todos os números pares de uma lista.")
    print("-" * 70)
    stop = False

    lista = []
    while not stop:
        lista.append(validadornumero("Digite um número!"))
        print("Digite sim se deseja continuar, ou qualquer outra tecla se deseja parar de inserir números.")
        verif = input().upper()
        if verif != "SIM":
            stop = True

    print("Sua lista:")
    print(lista)
    print("Agora, vamos retirar dela os números pares:")
    lista2 = []

    cont = 0

    while cont < len(lista):
        a = int(lista[cont])
        if a % 2 == 0:
            a = str(a)
            del(lista[cont])
        cont = cont + 1

    print(lista)







