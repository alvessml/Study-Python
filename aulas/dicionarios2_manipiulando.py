pessoa = {}

# Adicionar chave e valor
print('Adicionando chaves nome e sobrenome')
chave = 'nome'

pessoa[chave] = 'Samuel'
pessoa['sobrenome'] = 'Alves'

print(pessoa[chave])
print(pessoa['sobrenome'])

# Alterar o valor da chave
pessoa[chave] = 'Maria'
print('\nChave com nome alterado: ')
print(pessoa[chave])
print(pessoa['sobrenome'])

# Deletar chave
print('\nDeletando a chave sobre nome: ')
print(pessoa[chave])
# del pessoa['sobrenome']
# Irá ocorrer erro, pois a chave sobrenome não existe mais.
# print(pessoa['sobrenome']) 

# Leitura de chave, retorna None por padrão se não houver valor
print('\nLeitura do valor da chave: ')
print(pessoa[chave])
if pessoa.get('sobrenome') is None:
    print('Não existe.')
else:
    print(pessoa['sobrenome'])

