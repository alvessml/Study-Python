# Sets são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
# obs: - Não garante ordem dos elementos dentro do set.
#      - Eliminam valores duplicados normalmente
#      - Não tem índixes
#      - É interável (ou seja, pode usar: for, in, not in)


# Criando set vazio.
# obs: Set parece com dicionarios, mais não é.
s1 = set()
print(set, type(s1))


# Criando set com iteráveis
s2 = set('Luiz') # A saída será letras aleatórias dessa string, usando assim. Para resolver, veja abaixo dessa linha.
s3 = {'Luiz', 1, 2, 3} # obs: Não garante a ordem, ou seja, pode haver ordens aleatórias.
print(s3)


print()
# Métodos Úteis para usar no Set: add, update, clear, discart
s = set()
s.add('Samuel')
s.add(1)
s.add(7)
s.update({'Olá, mundo'}, (2, 3, 4, 5)) # obs: Muito parecido com o método add
s.clear() # Limpa o Set
s.update({'Olá, mundo'}, (1, 2, 3))
s.discard('Olá, mundo') # Discarta o valor
print(s)


print()
# Operadores Úteis: | (união ou union), & (intersection ou intersecção), - (diferença) e
# ^ (diferença simétrica, ou seja, em itens que não estão em ambos).
set1 = {1, 2, 3}
set2 = {2, 3, 4}
setUnion = set1 | set2
setIntersection = set1 & set2
setDiferenca = set1 - set2
setDiferenca1 = set2 - set1
setDiferencaSimetrica = set1 ^ set2

print(f"Essa é a união dos sets: {setUnion}") # Sem duplicação, visto que, o set elimina duplicação
print(f"Essa é a intersection dos sets: {setIntersection}") 
print(f"Essa é a diferença dos set1 - set2: {setDiferenca}") # obs: A ordem importa, set1 - set2 ou set2 - set1
print(f"Essa é a diferença dos set2 - set1: {setDiferenca1}") 
print(f"Essa é a diferença dos set: {setDiferencaSimetrica}") # Retorna os itens que não estão presentes em ambos.
 

