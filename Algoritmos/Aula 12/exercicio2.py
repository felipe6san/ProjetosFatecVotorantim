lista1 = []
lista2 = []
i = 0
for i in range(1, 11):
    lista1.append(i)
    lista2.append(i + 100)
conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(conjunto1.union(conjunto2))
