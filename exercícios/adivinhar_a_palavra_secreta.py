palavra_secreta = 'Carro'
letras_acertadas = ''
while True:
    letra_digitada = input('Digite uma letra: ').islower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(f'{letra_secreta}', end='')
        else:
            print('*', end='')
    print('\n')    












# palavra_secreta = 'carro'
# descobrindo_palavra = ''
# # while True:
# #     tentativa = input('Digite uma letra: ')
# #     for palavra in palavra_secreta:
# #         if tentativa == palavra:
# #             descobrindo_palavra += tentativa
# #         else:
# #             if tentativa in palavra_secreta:
# #                 descobrindo_palavra 
# #             else:
# #                 descobrindo_palavra += '*'
# #     print(f'Palavra secreta: {descobrindo_palavra}')
# # print("Você acertou!")
