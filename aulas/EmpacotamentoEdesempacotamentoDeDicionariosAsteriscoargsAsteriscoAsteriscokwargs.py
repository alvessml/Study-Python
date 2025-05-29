# Empacotamento e desempacotamento de dicionários
# Ex básico:
a, b, = 1, 2
a, b = b, a
print(a, b)

# ------------------------------
# print()
# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza'
# }

# a, b = pessoa
# print(f"chaves: {a} {b}")

# print()

# a, b = pessoa.values()
# print(f"valor da chave: {a} {b}")

# print()

# a, b = pessoa.items()
# print(f"tupla contendo a chave + valor: {a} e {b}")

# print()

# (a1, a2), (b1, b2) = pessoa.items()
# print(f"Desempacotamento contendo a chave + valor: {a1}: {a2} e {b1}: {b2}")



# ---------------------------------------
# Empacotar e desempacotar dicionários
# ---------------------------------------

print()
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.65
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# print()

#---------------------------------------------------
# kwargs - keyword arguments (argumentos nomeados)
# Explicação: **kwargs agrupa todos os argumentos
# nomeados extras (aqueles no formato chave=valor)
# em um dicionário dentro da função.
# Obs: **kwargs sempre é acompanhado de dois asteriscos 

# Exemplo de argumentos NÃO nomeados: 1, 2, 3, Samuel, Futebol
# Exemplo de argumentos nomeados: nome='Samuel'

def mostro_argumentos_nomeados(*args, **kwargs):
    print(f"Argumentos NÃO Nomeados: {args}")
    print("Argumentos nomeados: ", end='')
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}", end="  ")
    print()
mostro_argumentos_nomeados(1, 2, "não nomeado", nome='Samuel', sobrenome='Alves', nome_final='de Andrade')

mostro_argumentos_nomeados(**pessoas_completa)
