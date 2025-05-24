# introdução às Generator fuctions em python 
# O intuito é ter um meio de para a execução sem voltar ou sair da função

# Base Generador em dic
# generator = (n for n in range(1000000))
# print(next(generator))
# print(next(generator))


# Obs: Toda function que tem o yield é uma generator fuction
def generator(n=0):
    yield 1 # Pausar
    print('Continuando ...')
    yield 2 # Pausar 
    print ('Mais uma ...')
    yield 3 
    print('Vou terminar')
    return 'ACABOU'


gen = generator()
# print(gen.__iter__())
# Método __iter__()
# O método __iter__ em Python é um método especial usado para tornar um objeto iterável — ou seja, um objeto que pode ser percorrido com um for, in, list(), etc.

# Não dinâmicamente
# print("NÃO Dinâmicamente: ")
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

print("\nDinâmicamente: ")
for n in gen:
    print(n)


print("\n------------------------------\n")

# Criando um function que se comporta como um 'range':
def generator_max(n=0, maximum=10):
    while True:
        yield n
        n+=1
        if n >= maximum:
            return 'Acabooooooooooooou'
gen_max = generator_max()
print("\nDinâmicamente_max: ")
for n in gen_max:
    print(n)

gen_max_alterando = generator_max(n=5, maximum=8)
print("\nDinâmicamente_max alterando: ")
for n in gen_max_alterando:
    print(n)


print("\n------------------------------\n")

# Continuando o algoritmo usando o 'yield from functionAnterior()'

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5

def gen3(gen):
    yield from gen() # Importante, pois sem ele não funciona o 'g1 = gen3(gen1)'
    yield 60
    yield 70
    yield 80

# Tirando os () do gen e executando depois
# def gen3(gen):
#     yield from gen # Importante, pois sem ele não funciona o 'g1 = gen3(gen1)'
#     yield 60
#     yield 70
#     yield 80
# g1 = gen3(gen1())



g = gen2()

for n in g:
    print(n)

print()

g1 = gen3(gen1)

for n in g1:
    print(n)