from funct import primo

def qntPrimos(num):
    cont = 0
    for i in range(1, num + 1):
        if primo(i):
            cont + cont + 1
    return cont


valor = int(input("Digite seu número: "))
print(f"A quantidade de primos é de {valor}")

