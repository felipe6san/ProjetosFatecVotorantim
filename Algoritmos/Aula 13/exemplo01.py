'''Definição de funções'''
qtd = 5
x = 10
def linha(qtd):
    print(qtd, "dentro", x)
    for i in range(0,qtd):
        print("-", end='')
    print()

linha(25)
print()
print("== Uso de funções ==")
linha(30)