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
    print("-"*15)
    print("Somas repetidas")
    print("-"*15)

    # #Resolução Fluxograma (PROBLEMA: SE O SEGUNDO NÚMERO DER NEGATIVO, FICA PRESO NO SEGUNDO WHILE)
    # condicao = False
    # contador = 0
    # resultado = 0
    # while condicao == False:
    #     print("Digite o primeiro número.")
    #     a = input()
    #     print("Digite um número para multiplicar o primeiro.")
    #     b = input()
    #     if (is_int(a)) & (is_int(b)):
    #         condicao = True
    #         a = int(a)
    #         b = int(b)
    #         while contador != b:
    #             contador = contador + 1
    #             resultado = resultado + a
    #     else:
    #         input("Por favor, digite números! \n")
    #
    # print("\nO valor de sua multiplicação é: %d" % (resultado))

    # # Resolução Fluxograma (Resolvendo o problema)
    condicao = False
    contador = 0
    resultado = 0
    while condicao == False:
        print("Digite o primeiro número.")
        a = input()
        print("Digite um número para multiplicar o primeiro.")
        b = input()
        if (is_int(a)) & (is_int(b)):
            condicao = True
            a = int(a)
            b = int(b)
            if b > 0:
                while contador != b:
                    contador = contador + 1
                    resultado = resultado + a
            else:
                while contador != b:
                    contador = contador - 1
                    resultado = resultado - a
        else:
            input("Por favor, digite números! \n")

    print("\nO valor de sua multiplicação é: %d" % (resultado))

    # #Messagebox
    # a = simpledialog.askinteger("Input","Digite o primeiro número.")
    # b = simpledialog.askinteger("Input","Digite o número que irá multiplicar o primeiro.")
    # contador = 0
    # resultado = 0
    #
    # if b > 0:
    #     while contador != b:
    #         resultado = resultado + a
    #         contador = contador + 1
    # else:
    #     while contador != b:
    #         resultado = resultado -a
    #         contador = contador - 1
    #
    # simpledialog.messagebox.showinfo("Resultado","O resultado de sua multiplicação é: %d" % (resultado))
