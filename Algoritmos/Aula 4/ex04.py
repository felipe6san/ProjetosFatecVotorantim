salario = float(input("digite seu salário: R$"))
aumento_salario = float(input("digite o aumento percentual: "))
novo_salário = salario + salario * aumento_salario / 100
print(f"Seu novo salário é de: R${novo_salário:8.2f}")

