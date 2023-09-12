nome = input("Nome de Usúario: ")
idade = int(input("Digite sua idade: "))
print(f"{nome}", f"Sua idade é: {idade}")
if idade >= 60:
    print("Você já pode pagar 1/2 no cinema!")
elif idade >=30:
    print("Você está na metade da idade necessária para 1/2!")
else:
    print("Parabéns!! Você ainda é jovem!")

print("Acabou o Programa!!!!")

