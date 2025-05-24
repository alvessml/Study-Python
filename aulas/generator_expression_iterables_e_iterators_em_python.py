import sys # para verificar o tamanho da minha lista em BYTES

# Generator - são funções que sabem pausar em determinado ocasião
# Generator é igual ao iterator, mas o iterator não é igual ao generator

lista = [n for n in range(10000000)]
# Problema: 
# - Isso consome bastante memória ao criar uma lista comprehension


# Criando um generator com base na lista que é um problema, pois ocasiona 
# perda de memória
generator = (n for n in range(1000000))
# print("Isso é uma lista: ", lista)
print("Isso é um: ", generator)
print(sys.getsizeof(lista), "MB")
print(sys.getsizeof(generator), "MB") # Ele não salva todos os valores na memória, só se você chamar a função 
print(next(generator))
print(next(generator))

# Vantagem: No caso da lista, vocẽ pode acessar qualquer valor, pois estar salvo na memória, já o generator não.
