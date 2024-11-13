entrada = input('Digite um número: ')
try:
    numero_usr_int = int(entrada)
    par_ou_impar = entrada
    if entrada.isdigit():
        numero_usr_int = int(entrada)
        if numero_usr_int % 2 == 0:
            print(f'O número que você digitou é par.')
        else:
            print(f'O número que você digitou é ímpar.')                    
except:
    print('Erro! Digite um número qualquer.')