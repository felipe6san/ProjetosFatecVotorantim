def calcular_soma_multiplicacao(numero):
    soma = 0
    multiplicacao = 1

    for y in numero:
        if '0' <= y <= '9':
            digito = int(y)
            soma += digito
            multiplicacao *= digito
        else:
            print("Erro. Por favor, digite um número válido.")
            return None, None
    return soma, multiplicacao

numero = input("Digite seu RA: ")

soma, multiplicacao = calcular_soma_multiplicacao(numero)
if soma is not None:
    print(f"Soma: {soma}")
    print(f"Multiplicação: {multiplicacao}")
