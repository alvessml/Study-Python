# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Direita
# < - Esquerda
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

variavel = 'ABC'

# Exibe a variável sem formatação
print(f'{variavel}')

# Alinha à direita em um espaço de 10 caracteres
print(f'{variavel: >10}')

# Alinha à esquerda em um espaço de 10 caracteres
print(f'{variavel: <10}.')

# Centraliza em um espaço de 10 caracteres
print(f'{variavel: ^10}.')

# Formata um número com sinal, zero à esquerda, separador de milhar e 1 casa decimal
print(f'{1000.4873648123746:0=+10,.1f}')

# Converte um número para hexadecimal com 8 caracteres (maiúsculo) preenchidos com zeros à esquerda
print(f'O hexadecimal de 1500 é {1500:08X}')

# Exibe a representação "repr" da variável
print(f'{variavel!r}')
