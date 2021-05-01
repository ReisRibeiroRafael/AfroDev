dicionario = dict()
dicionario = {1: "oi", 2: "olá", 3: "hello", "C": 9}
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
dicionario[2] = "oláá"
print(dicionario)

for chave in dicionario:
    print(dicionario[chave])

for chave, valor in dicionario.items():
    print(chave,"-",valor)

dicionario.update({"1": 55, 2: "olá de novo"})
print(dicionario)