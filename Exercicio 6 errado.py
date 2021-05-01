from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import math
import pprint

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


def validadorsalario(texto):
    condicao = False
    print(texto)

    while not condicao:
        a = input()
        if is_float(a) and float(a) >= 0:
            return float(a)
        else:
            print("Por favor, digite um número válido.")


def validadordependente():
    condicao = False

    while not condicao:
        a = input()
        if is_int(a) and int(a) >= 0:
            return int(a)
        else:
            print("Por favor, digite um número válido.")


def dicionario():
    nomesalario = dict()
    cont = 1
    fim = False

    while not fim:
        nome = validadornome("Digite o nome da %dª pessoa." % cont)
        salario = validadorsalario(f"Digite agora o salário, em reais, de {nome}")
        nomesalario[nome] = salario
        cont = cont + 1
        print("Digite sair se deseja encerrar o programa. Se deseja continuar, digite qualquer outra coisa.")
        end = input().upper()
        if end == "SAIR":
            return nomesalario


if __name__ == '__main__':
    print("-" * 20)
    print("Desconto salarial")
    print("-" * 20)
    nomesalario = dicionario()
    salinss = dict()
    salirff = dict()
    saldependentes = dict()
    salliquido = dict()


    for nome, salario in nomesalario.items():
        # Dependentes
        print(f"\nDigite o número de dependentes de {nome}:")
        dependente = validadordependente()
        saldependentes[nome] = dependente * 189.59

        # INSS
        if salario <= 1100:
            salinss[nome] = salario * 0.075
        elif salario <= 2203.48:
            salinss[nome] = salario * 0.09
        elif salario <= 3305.22:
            salinss[nome] = salario * 0.12
        elif salario >= 6433.57:
            salinss[nome] = 6433.57 * 0.14
        else:
            salinss[nome] = salario * 0.14

        # IRFF
        if salario <= 1903.98:
            salirff[nome] = 0
        elif salario <= 2826.66:
            salirff[nome] = salario * 0.075
        elif salario <= 3751.05:
            salirff[nome] = salario * 0.15
        elif salario <= 4664.68:
            salirff[nome] = salario * 0.22
        else:
            salirff[nome] = salario * 0.275

        # Líquido
        salliquido[nome] = (salario - saldependentes[nome] - salinss[nome] - salirff[nome])

        # Arredondando
        nomesalario = round(nomesalario[nome], ndigits=2)
        salinss = round(salinss[nome], ndigits=2)
        salirff = round(salirff[nome], ndigits=2)
        saldependentes = round(saldependentes[nome], ndigits=2)
        salliquido[nome] = round(salliquido[nome], ndigits=2)

    print("\nLista com os salários brutos:")
    print(nomesalario)
    print("Lista com o quanto foi descontado pelo INSS:")
    print(salinss)
    print("Lista com o quanto foi descontado pelos dependentes:")
    print(saldependentes)
    print("Lista com o quanto foi descontado pelo IRRF:")
    print(salirff)
    print("Lista com o salário líquido:")
    print(salliquido)

