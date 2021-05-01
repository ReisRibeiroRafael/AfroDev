import math

def encryption(s):
    sqrt = len(s)
    lista = []
    contador = 0
    a = ""
    aux = 0
    nova_linha = 0

    sqrt = math.sqrt(sqrt)
    coluna = math.ceil(sqrt)
    linha = math.floor(sqrt)

    if coluna * linha < len(s):
        linha += 1

    while len(s) < coluna * linha:
        s = s + " "

    while len(lista) < coluna:
        if contador == aux + nova_linha:
            a = a + s[contador]
            aux = aux + coluna
        if len(a) == linha:
            lista.append(a)
            contador = 0
            nova_linha += 1
            aux = 0
            a = ""
        contador += 1

    result = []
    for z in range(len(lista)):
        result.append(lista[z].replace(" ",""))

    result = (" ".join(result))
    print(result)


if __name__ == '__main__':

    s = "feedthedog"

    result = encryption(s)

    # print(result)

    # print(result + '\n')

