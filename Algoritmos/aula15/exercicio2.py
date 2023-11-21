def verificaPositivo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'

print(verificaPositivo(int(input('Digite um numero: '))))
