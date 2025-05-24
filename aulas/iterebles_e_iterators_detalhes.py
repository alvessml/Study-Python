itereble = ['Eu', 'Tenho', '__iter__']
# iterator = itereble.__iter__() # tem __iter__ e __next__
iterator = iter(itereble)

# iterator só sabe entregar o próximo elemento

print(iterator) 
print(next(iterator)) # Mostra o 'Eu'
print(next(iterator)) # Mostra o 'Tenho'
print(next(iterator)) # Mostra o '__iter__'
print(next(iterator)) # Mostra o erro de StopIteration

