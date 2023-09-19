valor_compra = float(input("Digite o valor da sua compra: "))
if valor_compra <= 1000:
    desconto10 = valor_compra * 0.10
    valor_com_desconto10 = valor_compra - desconto10
    print(f"seu desconto é de: {valor_com_desconto10}")

elif valor_compra > 1000 and valor_compra < 5000:
    desconto20 = valor_compra * 0.20
    valor_com_desconto20 = valor_compra - desconto20
    print(f"seu desconto é de: {valor_com_desconto20}")

elif valor_compra > 5000:
    desconto30 = valor_compra * 0.30
    valor_com_desconto30 = valor_compra - desconto30
    print(f"Seu desconto é de : {valor_com_desconto30}")
else:
    print("Você não ganhou desconto")
