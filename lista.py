lista = []
lista.append(1)
lista.append("A")
lista.append(1.5)
print(lista)
del(lista[1])
print(lista)

lista.insert(0, "BB")
print(lista)
print(len(lista))
print(lista.pop(2))
lista[1] = "Olá"
print(lista)
print(lista[-1])
lista.clear()
print(lista)