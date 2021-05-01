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
    inteiro = False
    while inteiro == False:
            a = simpledialog.askinteger("Input","Digite um número!")
            b = simpledialog.askinteger("Input", "Digite mais um número!")
            if is_int(a) & is_int(b):
                inteiro = True
                a = int(a)
                b = int(b)
                soma = ((a+b)/2)
                soma = str(soma)
                messagebox.showinfo("Resultado","O valor de sua soma, dividido por 2, é igual a "+soma)
            else:
                print("Por favor, digite números!")