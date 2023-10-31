dicIdade = {}
maiorIdade = 0
while len(dicIdade) < 5:
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    dicIdade[sobrenome] = idade
for sobrenome, idade in dicIdade.items():
    if idade > maiorIdade:
        maiorIdade = idade
        maisVelho = sobrenome
print(f"A mais velho é o {maisVelho} com {maiorIdade} anos.")