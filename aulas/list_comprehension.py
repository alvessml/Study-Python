# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# Video de dúvidas do list comprehension no youtube: https://www.youtube.com/watch?v=1YbTDczvqco

# O que normalmente fazem para imprimir lista
lista = []
for num in range(10):
    lista.append(num)
print(lista)


# Usando List comprehension
lista_comprehension = [numero * 2 for numero in range(10)]
print(lista_comprehension)