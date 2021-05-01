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
    print("-"*115)
    print("Faça um algoritmo de uma lâmpada de emergencia. A partir de um sinal, indique se a luz esta acessa ou "
          "apagada.")
    print("-"*115)

    sinal = '0'
    verificacao = '0'

    while verificacao != '1':
        print("A energia está ligada? Digite 1 para sim e 2 para não.")
        sinal = input()

        if sinal != '1' and sinal != '2':
            print("Opção inválida.\n")
        else:
            if sinal == '1':
                print("\nAs lâmpadas de emergência estão desligadas.")
            else:
                print("\nAs lâmpadas de emergência estão ligadas.")
            print("Digite 1 caso deseja encerrar a verificação e qualquer outra tecla se deseja continuar.")
            verificacao = input()

    print("\nSistema de emergência desligado.")


