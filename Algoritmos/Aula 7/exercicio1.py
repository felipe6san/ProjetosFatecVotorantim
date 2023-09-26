numero = int(input("Digite a quantia de números: "))
total = 0
E = 0
if numero > 0:
    for i in range(1, numero + 1):
        E = (2 ** i)
        total = total + E
    print(f" Seu valor E é de: {total} ")


