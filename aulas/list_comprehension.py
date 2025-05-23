# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# O que normalmente fazem para imprimir lista
lista = []
for num in range(10):
    lista.append(num)
print(lista)


# Usando List comprehension
lista_comprehension = [numero * 2 for numero in range(10)]
print(lista_comprehension)