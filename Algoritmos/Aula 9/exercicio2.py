lista = []

for i in range(5):
    lista.append(int(input(f"Digite o número {i+1}: ")))
print(f"O maior valor é {max(lista)}, está no indice {lista.index(max(lista))}")
