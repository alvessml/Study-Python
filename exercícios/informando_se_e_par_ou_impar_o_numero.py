entrada = input('Digite um número: ')
try:
    numero_usr_int = int(entrada)
    par_impar = numero_usr_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {numero_usr_int} é {par_impar_texto}.')              
except:
    print('Erro! Digite um número qualquer.')