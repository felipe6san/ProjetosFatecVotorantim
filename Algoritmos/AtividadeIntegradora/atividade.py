import random
def mensagemMotivacional():
    mensagens = [
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    mensagem_aleatoria = random.choice(mensagens)
    print(mensagem_aleatoria)

mensagemMotivacional()