nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if 0 <= media < 3.0:
    print(f"Média: {media:5.2f} - Você foi reprovado!")
elif 3.0 <= media < 7.0:
    nota_exam = 12 - media
    print(f"Média {media:5.2f} - Você ficou para o exame de recuperação! Nota necessária para passar: {nota_exam}")
elif 7.0 <= media <= 10:
    print(f"Média {media:5.2f} - Você foi aprovado!")
else:
    print(f"Média {media:5.2f} - Sua média é inválida!")
