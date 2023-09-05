ano_de_nascimento = int(input("Ano de nascimento "))
ano_atual = int(input("Ano atual "))
idade = ano_atual - ano_de_nascimento
idade_mes = idade * 12
idade_dias = idade * 365
idade_semana = idade * 53
print(f"a sua idade é de: {idade} anos")
print(f"a sua idade é de: {idade_mes} meses")
print(f"a sua idade é de: {idade_dias} dias" )
print(f"a sua idade é de: {idade_semana} semanas")
