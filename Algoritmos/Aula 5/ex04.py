x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

if (x < y+z) and (y < x+z) and (z < x+y):
    if x == y == z:
        print("Ele é um triângulo equilátero!")
    elif (x == y) or (x == z) or (y == z):
        print("Ele é um triângulo isóseles!")
    else:
        print("ele é um triângulo escaleno!")
else:
    print("Não é um triângulo!")
