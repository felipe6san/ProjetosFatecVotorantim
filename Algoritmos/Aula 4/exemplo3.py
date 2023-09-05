from math import pow, sqrt
x1 = int(input("Entre com o x1: "))
y1 = int(input("Entre com o y1: "))
x2 = int(input("Entre com o x2: "))
y2 = int(input("Entre com o y2: "))
dx = x2 - x1
dy = y2 - y1
distancia = sqrt(pow(dx, 2) + pow(dy, 2))
print(f"A distancia entre os pontos é de= {distancia}")
