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

def menu():
    print("-"*30)
    print("Menu para cálculo de área!")
    print("-"*30)
    print("Digite um número de acordo com o objeto a ter sua área calculada:")
    print("1 para retângulo.")
    print("2 para quadrado.")
    print("3 para círculo.")
    print("4 para triângulo.")
    print("5 para sair do programa.")
    print("-" * 30)


def retangulo(verificador):
    while not verificador:
        print("Digite o valor da base:")
        base = input()
        print("Digite o valor da altura:")
        altura = input()
        if is_float(base) and is_float(altura):
            base = float(base)
            altura = float(altura)
            if base > 0 and altura > 0:
                base = float(base)
                altura = float(altura)
                verificador = True
                area = base * altura
                return area
            else:
                print("Digite dois números maiores que 0.")
        else:
            print("Digite dois números maiores que 0.")


def quadrado(verificador):
    print("Digite o valor do lado do quadrado.")
    while not verificador:
        lado = input()
        if is_float(lado):
            lado = float(lado)
            if lado > 0:
                area = lado * lado
                return area
            else:
                print("Digite um número maior que 0.")
        else:
            print("Digite um número maior que 0.")


def circulo(diametro):
    try:
        is_float(diametro)
    except:
        print("Por favor, digite um valor de diâmetro válido.")
    else:
        diametro = float(diametro)
        if diametro > 0:
            verificador = True
            area = math.pi * diametro * diametro / 4
            print("A área do seu círculo é igual a %.2f u.a." % area)
            print("Digite qualquer tecla para continuar.")
        else:
            print("Por favor, digite um valor de diâmetro válido.")
    finally:
        return verificador


def triangulo(base,altura):
    try:
        is_float(base)
        is_float(altura)
    except:
        print("Por favor, digite valores válidos para a base e a altura.")
    else:
        base = float(base)
        altura = float(altura)
        if base > 0 and altura > 0:
            verificador = True
            area = base * altura / 2
            print("O valor da área do seu triângulo é igual a %.2f u.a." % area)
            print("Digite qualquer tecla para continuar.")
        else:
            print("Por favor, digite valores válidos para a base e a altura.")
    finally:
        return verificador

if __name__ == '__main__':
    condicao = False

    while not condicao:
        menu()
        opcao = input()
        if is_int(opcao):
            opcao = int(opcao)
            verificador = False
            if opcao == 1: #Retângulo
                area = retangulo(verificador)
                print("A área do seu retângulo é igual a %.2f u.a." % area)
                print("Digite qualquer tecla para continuar.")
                input()
            elif opcao == 2: #Quadrado
                area = quadrado(verificador)
                print("A área do seu quadrado é igual a %.2f u.a." % area)
                print("Digite qualquer tecla para continuar.")
                input()
            elif opcao == 3: #Círculo
                print("Digite o valor do diâmetro do círculo!")
                while not verificador:
                    diametro = input()
                    verificador = circulo(diametro)
                    input()
            elif opcao == 4: #Triângulo
                while not verificador:
                    print("Digite o valor da base do triângulo.")
                    base = input()
                    print("Digite o valor da altura do triângulo.")
                    altura = input()
                    verificador = triangulo(base,altura)
                    input()
            elif opcao == 5: #Sair
                condicao = True
                print("Fim.")
            else:
                print("Por favor, digite um número válido! O menu será exibido novamente.")
        else:
            print("Por favor, digite um número válido! O menu será exibido novamente.")