palavra_secreta = 'carro'
letras_acertadas = ''
num_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('\n')  

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra secreta era: ', palavra_secreta)
        print('Número de tentativas: ', num_tentativas)
        letras_acertadas = ''
        num_tentativas = 0
        break  












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
