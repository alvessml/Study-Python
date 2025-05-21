perguntas = [
    {
        'Pergunta': 'Quanto é 25*3?',
        'Opções': ['70', '75', '85', '80'],
        'Resposta': '75'
    },
    {
        'Pergunta': 'Quanto é 5*3?',
        'Opções': ['16', '18', '15', '20'],
        'Resposta': '15'
    },
    {
        'Pergunta': 'Quanto é 2*3?',
        'Opções': ['6', '8', '9', '7'],
        'Resposta': '6'
    }
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")
    print()

    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print("Acertou!")
    else:
        print("Errou")

    print()

print(f"Você acertou {qtd_acertos} de {len(perguntas)} perguntas")