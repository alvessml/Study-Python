nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[(len(nome)):: -1]}')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
    print(f'Primeira letra do seu nome é {nome[0]}')
    print(f'Ultima letra do seu nome é {nome[-1]}')
else:
    print('Erro! Digite novamente!')
