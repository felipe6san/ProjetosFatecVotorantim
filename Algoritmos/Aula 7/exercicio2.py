soma_altura = 0
soma_peso = 0
imc = 0
for i in range(1, 6):
    altura = float(input(f"Pessoa {i} digite sua altura: "))
    soma_altura = soma_altura + altura
    peso = float(input(f"Pessoa {i} digite seu peso: "))
    soma_peso = soma_peso + peso
    imc = peso / (altura * altura)
peso_medio = soma_peso / 5
altura_media = soma_altura / 5
print(f"A altura média é de: {altura_media}")
print(f"A peso médio é de: {peso_medio}")

