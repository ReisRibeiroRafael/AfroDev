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
    print("Digite três números e diga qual o maior.")
    print("-"*50)

    # #Resolução idêntica ao fluxograma
    # condicao = False
    # while condicao == False:
    #     print("Digite o primeiro número")
    #     a = input()
    #     print("Digite outro número")
    #     b = input()
    #     print("Digite outro número")
    #     c = input()
    #
    #     if is_int(a) & is_int(b) & is_int(c):
    #         a = int(a)
    #         b = int(b)
    #         c = int(c)
    #         if (a != b) & (a != c) & (b != c):
    #             condicao = True
    #         else:
    #             print("Por favor, digite 3 números diferentes!")
    #     else:
    #         print("Por favor, digite um número nas 3 etapas!")
    #
    # if a > b:
    #     if a > c:
    #         print("\n %d é o maior número!" % (a))
    #     else:
    #         print("\n %d é o maior número!" %(c))
    # else:
    #     if b > c:
    #         print("\n %d é o maior número!" % (b))
    #     else:
    #         print("\n %d é o maior número!" % (c))

    # Resolução posterior
    print("Digite um número: ")

    condicao = False
    while condicao == False:
        a = input()
        if is_int(a):
            condicao = True
            a = int(a)
            maior = a
            menor = a
        else:
            print("Por favor, digite um número válido!")

    print("Digite outro número!")
    while condicao == True:
        b = input()
        if is_int(b):
            condicao = False
            b = int(b)
            if b > maior:
                maior = b
            if b < menor:
                menor = b
        else:
            print("Por favor, digite um número válido!")

    print("Digite o último número!")
    while condicao == False:
        c = input()
        if is_int(c):
            condicao = True
            c = int(c)
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        else:
            print("Por favor, digite um número válido!")

    print("O maior número digitado foi %d e o menor foi %d." % (maior,menor))

    # Resolução com dialogbox
    # a = simpledialog.askinteger("Input","Digite um número!")
    # maior = a
    # menor = a
    #
    # b = simpledialog.askinteger("Input","Digite outro número.")
    # if b > maior:
    #     maior = b
    # if b < menor:
    #     menor = b
    #
    # c = simpledialog.askinteger("Input","Digite outro número.")
    # if c > maior:
    #     maior = c
    # if b < menor:
    #     menor = c
    #
    # maior = str(maior)
    # menor = str(menor)
    #
    # if maior == menor:
    #     simpledialog.messagebox.showwarning("Erro!","Você digitou 3 números iguais! O número digitado foi "+maior+".")
    # else:
    #     simpledialog.messagebox.showinfo("Input","O maior número digitado foi "+maior+" e o menor número digitado foi "+menor+".")
