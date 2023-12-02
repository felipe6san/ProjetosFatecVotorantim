def calcular_patos_coelhos(total_cabecas, total_pes):
    coelhos = (total_pes - 2 * total_cabecas) / 2
    patos = total_cabecas - coelhos
    return int(patos), int(coelhos)

total_cabecas = 24 * 2 + 5
total_pes = 24 * 3 + 7
patos, coelhos = calcular_patos_coelhos(total_cabecas, total_pes)

print(f"Total de patos: {patos}")
print(f"Total de coelhos: {coelhos}")