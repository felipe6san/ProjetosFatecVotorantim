aposento_largura = float(input("Digite a largura do aposento: "))
aposento_comprimento = float(input("Digite o comprimento do aposento: "))
altura_parede = 2.80
area_parede = 2 * altura_parede * (aposento_comprimento + aposento_largura)
altura_porta = 0.80
largura_porta = 2.10
area_porta = largura_porta * altura_porta
area_pintada = area_parede - area_porta
cobertura_por_litro = 3
litros_de_tinta = area_pintada / cobertura_por_litro
quantidade_de_latas = litros_de_tinta / 18
print(f"Área de paredes a ser pintada: {area_pintada:.2f} metros quadrados")
print(f"Quantidade de litros necessários de tinta: {litros_de_tinta:.2f} litros de tinta")
print(f"Quantidade de latas necessárias: {quantidade_de_latas:.2f} latas de tinta")
