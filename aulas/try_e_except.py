"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorre algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    # Tenta converter a entrada para float
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    # Lida com o erro caso a entrada não seja um número válido
    print('Erro: Isso não é um número válido.')
