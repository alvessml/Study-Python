while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')


    num_1_valido = None
    num_1_float = 0
    try:
        num_1_float = float(num_1)
        num_1_valido = True
    except:
        num_1_valido = None


    num_2_valido = None
    num_2_float = 0
    try:
        num_2_float = float(num_2)
        num_2_valido = True
    except:
        num_2_valido = None


    if num_1_valido is None:
        print('Primeiro número digitado está inválido!')
        continue
    elif num_2_valido is None:
        print('Segundo número digitado está inválido!')
        continue
    elif num_1_valido and num_2_valido is None:
        print('Os dois números digitados estar inválido!')
        continue


    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}') 
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')


    sair = input('Quer sair? Digite [s]im: ').lower().startswith('s')
    if sair is True:
        break
    
    print()