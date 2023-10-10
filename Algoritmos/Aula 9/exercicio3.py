from random import randint
dado = [0]*7

for i in range(0, 6001):
    dadoLado = randint(1, 6)
    dado[dadoLado] = dado[dadoLado]+1

p = [0]*7

for i in range(1, 7):
    p[i] = (dado[i] / 6000) * 100
    print(f"{i}) tem o percentual de {p[i]:.2f}")
