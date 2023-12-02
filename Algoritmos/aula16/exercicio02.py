def primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def qntPrimos(valor):
    contador = 0
    for qnt in range(valor + 1):
        if primo(qnt):
            contador += 1
    return contador


valor = 24 * 2 + 5
listaPrimos = [qnt for qnt in range(valor + 1) if primo(qnt)]
somaPrimos = sum(listaPrimos)

print(f"Lista de primos: {listaPrimos}")
print(f"Soma dos primos: {somaPrimos}")
