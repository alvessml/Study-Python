import copy

from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    #{**p} -> Expande o dicionários, tanto a chave quantos os dados da chave
    #round(x,y) -> Limita as casas de números decimais
    #p['preco'] -> Para cada p (dicionários) na chave preços, aumentar 10% em cima valor 
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# PAREI NO MINUTO 6 DA AULA 162