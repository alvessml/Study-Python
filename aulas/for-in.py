# Estruta básica
# O for recebe sempre algo interável para interar
# texto = 'Python'

# for letra in texto:
#     print(letra)



texto = 'Python'
novo_texto_asterisco = ''
for letra in texto:
    novo_texto_asterisco += f'*{letra}'
    print(f'{letra}', end='')

print(f'\n{novo_texto_asterisco}')