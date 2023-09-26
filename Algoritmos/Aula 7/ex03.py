soma = 0
medio = 0
idadeQnt = int(input("Digite a quantia de idades: "))
for i in range(1, idadeQnt + 1):
    n = int(input(f"Entre com a sua {i} idade: "))
    soma = soma + n
media = soma / idadeQnt
print(f" A média é de: {media}")