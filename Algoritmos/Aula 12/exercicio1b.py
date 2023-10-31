dicIdade = {}
idadeTotal = 0
while len(dicIdade) < 5:
    nome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    dicIdade[nome] = idade
    idadeTotal += idade

media = idadeTotal / len(dicIdade)

for nome, idade in dicIdade.items():
    if idade > media:
        print(f"{nome} tem idade superior a média.")