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
    print("-"*50)
    print("Digite dois números inteiros e subtraia o maior do menor.")
    print("-"*50)

    # #Resolução Fluxograma
    # condicao = False
    # while condicao == False:
    #     print("Digite o primeiro número.")
    #     a = input()
    #     print("Digite outro número número.")
    #     b = input()
    #
    #     if (is_int(a)) & (is_int(b)):
    #         a = int(a)
    #         b = int(b)
    #         if a != b:
    #             condicao = True
    #         else:
    #             print("Por favor, digite 2 números diferentes! \n")
    #     else:
    #         print("Por favor, digite 2 números! \n")
    #
    # if a > b:
    #     resultado = a - b
    #     print("%d - %d = %d" % (a,b,resultado))
    # else:
    #     resultado = b - a
    #     print("%d - %d = %d" % (b, a, resultado))

    #Resolução messagebox
    # condicao = False
    # while condicao == False:
    #     a = simpledialog.askinteger("Input", "Digite um número!")
    #     b = simpledialog.askinteger("Input", "Digite outro número!")
    #
    #     if a == b:
    #         simpledialog.messagebox.showwarning("Erro!","Por favor, digite 2 números diferentes!")
    #     else:
    #         condicao = True
    #
    # if a > b:
    #     resultado = a - b
    #     simpledialog.messagebox.showinfo("Resultado","%d - %d = %d" % (a,b,resultado))
    # else:
    #     resultado = b - a
    #     simpledialog.messagebox.showinfo("Resultado","%d - %d = %d" % (b,a,resultado))


