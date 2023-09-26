while True:
    base = float(input("Entre com a base: "))
    if base > 0:
        break
    print("O valor digitado é inváido!")
while True:
    altura = float(input("Entre com a altura: "))
    if altura > 0:
        break
    print("O valor digitado é inváido!")
area = (base * altura) / 2
print(f"Á área do triângulo é {area:5.2f}")
