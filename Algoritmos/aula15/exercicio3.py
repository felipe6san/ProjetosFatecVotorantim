def somaImposto(taxaImposto, custo):
    custo += custo * (taxaImposto / 100)
    return f"{custo:.2f}"

valorFinal = somaImposto((int(input('Digite a taxa do imposto em %: '))),
                  (int(input('Informe o custo do produto: '))))

print(valorFinal)
