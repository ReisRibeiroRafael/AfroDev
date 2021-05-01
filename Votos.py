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
    print("-"*75)
    print("Escreva um algoritmo para ler o número de votos brancos, nulos e válidos.")
    print("-"*75)

    # Resolução Fluxograma - Problema: Fiz como se fosse computar em tempo real, votos são inseridos manualmente
    print("Por gentileza, informe o número de habitantes da região.")
    habitantes = input()

    while is_int(habitantes) == False:
        print("Por favor, digite um número válido!")
        habitantes = input()

    while int(habitantes) <= 0:
        print("Por favor, digite um número válido!")
        habitantes = input()
        if is_int(habitantes) == False:
            while is_int(habitantes) == False:
                print("Por favor, digite um número válido!")
                habitantes = input()

    habitantes = int(habitantes)
    nulo = 0
    valido = 0
    branco = 0

    while habitantes > (nulo + valido + branco):
        print("Deseja votar em algum candidato? Digite 1 para sim e 2 para não.")
        opcao = input()

        while (opcao != '1') & (opcao != '2'):
            print("Por favor, digite 1 se deseja votar em um candidato e 2 se não deseja votar.")
            opcao = input()

        opcao = int(opcao)

        if opcao == 1:
            valido = valido + 1
            opcao = 0
        else:
            print("Deseja votar em branco? Digite 1 para sim e 2 para não.")
            opcao = input()
            while (opcao != '1') & (opcao != '2'):
                print("Por favor, digite 1 se deseja votar em um candidato e 2 se não deseja votar.")
                opcao = input()

            opcao = int(opcao)

            if opcao == 1:
                branco = branco + 1
                opcao = 0
            else:
                nulo = nulo + 1
                opcao = 0

    percentualValidos = int(valido)*100/habitantes
    percentualNulos = int(nulo)*100/habitantes
    percentualBrancos = int(branco)*100/habitantes

    print("\nPercentual de votos válidos: %d%%" %(percentualValidos))
    print("Percentual de votos nulos: %d%%" %(percentualNulos))
    print("Percentual de votos brancos: %d%%" %(percentualBrancos))

    #Resolução melhorada
    # condicao = 1
    # while condicao == 1:
    #     print("Insira o número de habitantes:")
    #     habitantes = input()
    #
    #     while is_int(habitantes) == False:
    #         print("Por favor, digite um número válido!")
    #         habitantes = input()
    #
    #     while int(habitantes) <= 0:
    #         print("Por favor, digite um número válido!")
    #         habitantes = input()
    #         if is_int(habitantes) == False:
    #             while is_int(habitantes) == False:
    #                 print("Por favor, digite um número válido!")
    #                 habitantes = input()
    #
    #     habitantes = int(habitantes)
    #
    #     print("Digite o número de votos válidos:")
    #     valido = input()
    #     while is_int(valido) == False:
    #         print("Por favor, digite um número válido!")
    #         valido = input()
    #
    #     while int(valido) < 0:
    #         print("Por favor, digite um número válido!")
    #         valido = input()
    #         if is_int(valido) == False:
    #             while is_int(valido) == False:
    #                 print("Por favor, digite um número válido!")
    #                 valido = input()
    #
    #     valido = int(valido)
    #     print("Votos computados até o momento: %d" % (valido))
    #     print("Votos a serem computados: %d" % (habitantes - valido))
    #     print("\nDigite o número de votos nulos:")
    #     nulo = input()
    #     while is_int(nulo) == False:
    #         print("Por favor, digite um número válido!")
    #         nulo = input()
    #
    #     while int(nulo) < 0:
    #         print("Por favor, digite um número válido!")
    #         nulo = input()
    #         if is_int(nulo) == False:
    #             while is_int(nulo) == False:
    #                 print("Por favor, digite um número válido!")
    #                 nulo = input()
    #
    #     nulo = int(nulo)
    #     print("Votos computados até o momento: %d" % (valido + nulo))
    #     print("Votos a serem computados: %d" % (habitantes - valido - nulo))
    #     print("\nDigite o número de votos brancos:")
    #     branco = input()
    #     while is_int(branco) == False:
    #         print("Por favor, digite um número válido!")
    #         branco = input()
    #
    #     while int(branco) < 0:
    #         print("Por favor, digite um número válido!")
    #         branco = input()
    #         if is_int(branco) == False:
    #             while is_int(branco) == False:
    #                 print("Por favor, digite um número válido!")
    #                 branco = input()
    #
    #
    #     if habitantes == int(valido) + int(branco) + int(nulo):
    #         percentualValidos = int(valido) * 100 / habitantes
    #         percentualNulos = int(nulo)*100/habitantes
    #         percentualBrancos = int(branco)*100/habitantes
    #
    #         print("\nPercentual de votos válidos: %d%%" %(percentualValidos))
    #         print("Percentual de votos nulos: %d%%" %(percentualNulos))
    #         print("Percentual de votos brancos: %d%%" %(percentualBrancos))
    #         condicao = 0
    #     else:
    #         print("Tá achando que é o Trump pra querer manipular as eleições? Contabiliza os votos direito!\n")