numA = float(input("Digite seu primeiro número: "))
numB = float(input("Digite seu segundo número: "))
if numA < numB:
    print(f"Seu menor número é:{numA}")
elif numB < numA:
    print(f"Seu menor número é:{numB}")
else:
    print("Os números são iguais!")
