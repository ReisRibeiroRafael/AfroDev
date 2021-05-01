# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from Carro import Carro
from Pessoa import Pessoa
from Restaurante import Restaurante
from Cofrinho import Cofrinho
from ContaBancaria import ContaBancaria

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #ContaBancaria
    print("Bem-Vindo. Digite o seu número da conta.")
    conta = input()
    c = ContaBancaria(conta)
    opcao = 0

    while opcao != 4:
        print("Digite 1 para consultar saldo, 2 para adicionar dinheiro, 3 para retirar e 4 para finalizar.")
        opcao = int(input())
        if opcao == 1:
            print("R$ %.2f" % c.consultar())
        elif opcao == 2:
            print("Quanto deseja adicionar?")
            dinheiro = float(input())
            c.adicionar(dinheiro)
            print("Novo saldo:")
            print("R$ %.2f" % c.consultar())
        elif opcao == 3:
            print("Quanto deseja retirar?")
            dinheiro = float(input())
            checagem = c.retirar(dinheiro)
            if not checagem:
                print("Desculpe, você não tem dinheiro suficiente.")
            else:
                print("Novo saldo:")
                print("R$ %.2f" % c.consultar())
        elif opcao == 4:
            print("Obrigado por confiar em nosso serviço.")
        else:
            print("Operação inválida.")


    print("Vamos tentar assaltar o banco.")
    # c.__saldo() = 300000
    print(c.consultar())
    print(c.__saldo())

    #Cofrinho
    # quebrar = False
    # d = Cofrinho("0", "0")
    #
    # while not quebrar:
    #     print("Quanto de dinheiro, em reais, você gostaria de adicionar no cofrinho?")
    #     dinheiro = float(input())
    #     d.adicionar(dinheiro)
    #     print("Digite 1 se deseja adicionar mais dinheiro, 2 se deseja pesar o cofrinho ou 3 se deseja quebrá-lo.")
    #     opcao = input()
    #     if opcao == "2":
    #         d.peso = 3
    #         print("O seu cofrinho pesa %.2f gramas" % d.pesar())
    #         print("Deseja adicionar mais dinheiro (1) ou quebrar o cofrinho (3)?")
    #         opcao = input()
    #     if opcao == "3":
    #         print("Você tinha no cofrinho R$ %.2f" % d.quebrar_cofrinho())
    #         quebrar = True
    #
    # print("Quer criar moedas magicamente? Tente digitar quantas moedas você quer que apareça:")
    # d.__saldo = input()
    # print(d.__saldo)
    # print(d.quebrar_cofrinho())


    #Restaurante
    # a = Restaurante("Pé de Fava", 2, "Guarulhos")
    # print(a.get_estrelas())
    # a.set_estrelas(1)
    # print(a.get_estrelas())
    # a.jacquin()
    # print(a.get_nome())
    # print(a.get_estrelas(), "estrelas")



    #Pessoa
    # a = Pessoa("180", 25, "Salvador")
    # print(a.get_altura())
    # a.set_altura("178")
    # print(a.get_altura())
    # print(a.get_idade())
    # a.aniversario()
    # print(a.get_idade())


    # c = Carro("Pálio", "Vermelho", 1.0)
    # print(c.get_modelo())
    # c.set_modelo("Ferrari")
    # print(c.get_modelo())
    # d = Carro("Uno com escada em cima", "Branco", 2.0)
    # print(d.get_modelo()


