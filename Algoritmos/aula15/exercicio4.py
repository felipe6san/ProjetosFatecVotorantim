def conversao(hora, minuto):
    if 0 < hora >= 24 or 0 < minuto >= 60:
        return 'Digite uma hora válida'
    if hora <= 12:
        if hora == 12:
            hora = 0
        notacao = 'A'
    if hora > 12:
        hora -= 12
        notacao = 'P'
    return f"{hora:02d}:{minuto:02d} {notacao}.M"

def saida(continuar):
    while continuar == 'S':
        print(conversao(int(input('Digite o tempo em horas: ')),
              (int(input('Digite o tempo em minutos: ')))))
        continuar = input('Continuar (S/N)? ')

saida('S')
