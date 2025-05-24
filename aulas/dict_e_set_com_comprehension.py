produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

# Comprehension:
dc = {                   # Irá deixar tudo com letras maiúsculas nas strings
    chave: valor.upper() # .upper() será conhecido se executar a linha de condição abaixo também
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dc)

# -------------------------------------------------------------------
sc = {i**2 for i in range(10)} # ou sc = set(range(10))
print(sc)