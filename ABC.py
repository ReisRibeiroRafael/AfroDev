# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# Forma errada -> Eu não mostrava qual o valor da divisão
    i = False
    print("-"*28)
    print("Somar 2 números e dividir pelo terceiro.")
    print("-"*28)
    while i == False:
        a = int(input("Digite um número maior que 10: "))

        if (is_int(a)) & (a > 10):
            b = int(input("Digite outro número! "))

            if is_int(b):
                c = int(input("Digite um número diferente de 0. "))

                if (is_int(c)) & (c != 0):
                    resultado = (a+b)/c
                    i = True

                    if resultado < 4:
                        print("")
                        print("O primeiro número somado ao segundo e dividido pelo terceiro é menor que 4.")
                    else:
                        print("")
                        print("O primeiro número somado ao segundo e dividido pelo terceiro é maior ou igual a 4.")

                else:
                    print("Operação inválida!")
                    print("")
            else:
                print("Operação inválida!")
                print("")
        else:
            print("Operação inválida!")
            print("")

# # Forma certa (eu acho kkkkkkk)
# i = False
# print("-" * 28)
# print("Somar 2 números e dividir pelo terceiro.")
# print("-" * 28)
# while i == False:
#     a = input("Digite um número maior que 10: ")
#
#     if is_int(a):
#         a = int(a)
#         if a > 10:
#             b = int(input("Digite outro número! "))
#
#             if is_int(b):
#                 b = int(b)
#                 c = input("Digite um número diferente de 0. ")
#
#                 if is_int(c):
#                     c = int(c)
#                     if c != 0:
#                         resultado = (a + b) / c
#                         i = True
#
#                         if resultado < 4:
#                             print("")
#                             print(
#                                 "O primeiro número somado ao segundo e dividido pelo terceiro é menor que 4, e igual a %d." % (
#                                     resultado))
#                         else:
#                             print("")
#                             print(
#                                 "O primeiro número somado ao segundo e dividido pelo terceiro é maior ou igual a 4, e igual a %d." % (
#                                     resultado))
#                     else:
#                         print("Operação inválida!")
#                         print("")
#                 else:
#                     print("Operação inválida!")
#                     print("")
#             else:
#                 print("Operação inválida!")
#                 print("")
#         else:
#             print("Operação inválida!")
#             print("")
#     else:
#         print("Operação inválida!")
#         print("")

# Versão de treino que eu fiz antes da aula
# dez = False
# while dez == False:
#         a = simpledialog.askinteger("Input","Digite um número maior que 10.")
#         if a == None:
#             break
#         if a > 10:
#             dez = True
#             b = simpledialog.askinteger("Input","Digite outro número.")
#             if b == None:
#                 break
#             zero = True
#             while zero == True:
#                 c = simpledialog.askinteger("Input","Digite um número para dividir a soma dos outros 2!")
#                 if c == None:
#                     break
#                 if c != 0:
#                     zero = False
#                     resultado = (a+b)/c
#                     simpledialog.messagebox.showinfo("Resultado","O valor de sua divisão é de "+str(resultado))
#                 else:
#                     simpledialog.messagebox.showerror("Erro!","Por favor, digite um número diferente de 0")
#         else:
#             simpledialog.messagebox.showerror("Erro!","Por favor, digite um número maior que 10.")
