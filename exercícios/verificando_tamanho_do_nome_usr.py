nome = input('Digite seu nome: ')
tam_nome = len(nome)

try:
    if tam_nome > 1:
        if tam_nome <= 4:
            print('Seu nome é curto')
        elif tam_nome <= 6:
            print('Seu nome é normal')
        else:
            print('Seu nome é muito grande')
except:
    print('Digite somente letras!')