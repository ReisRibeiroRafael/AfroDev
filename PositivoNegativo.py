# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("-" * 50)
    print("Digite um número e diga se ele é positivo ou negativo.")
    print("-" * 50)

    #Fluxograma
    condicao = False
    print("Digite um número diferente de 0.")
    while condicao == False:
        a = input()

        if is_int(a):
            a = int(a)
            if a != 0:
                condicao = True
            else:
                print("Por favor, digite um número diferente de 0.")
        else:
            print("Por favor, digite um número diferente de 0.")

    if a > 0:
        print("\n%d é um número positivo." % (a))
    else:
        print("\n%d é um número negativo." %(a))


    #Messagebox
    # numero = False
    # while numero == False:
    #     a = simpledialog.askinteger("Número","Digite um número diferente de 0.")
    #     if a == None:
    #         break
    #     if a == 0:
    #         simpledialog.messagebox.showerror("Zero","O número precisa ser diferente de 0")
    #     else:
    #         numero = True
    #         if a > 0:
    #             simpledialog.messagebox.showinfo("Resultado","O número digitado é positivo!")
    #         else:
    #             simpledialog.messagebox.showinfo("Resultado","O número digitado é negativo!")


