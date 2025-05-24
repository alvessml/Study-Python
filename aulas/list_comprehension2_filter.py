from pprint import pprint 

# Deixa o print mais bonito para quem manipular list e dic ao mesmo tempo
def p(v):
    pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# p(novos_produtos)

# print()

# pprint(novos_produtos)

# # print(novos_produtos)
# # print(*novos_produtos, sep='\n')



#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
lista = [n for n in range(10) if n < 5] # List comprehension + filter

# macete lista = [nessaEsquerdaEmapeamento for i in range(x) nessaDiretaEfilter]

# Ex:

novos_produtos_com_filter = [# acessando valor
    {**produto, 'preco': produto['preco'] * 1.5} # com 1 asterisco imprime some as chaves e com 2 asteriscos imprime chaves e valores
    if produto['preco'] >= 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.5) > 10 # filter preco acima de 10
]

print("Printe NORMAL: ", novos_produtos_com_filter)
print()
print("Print com PPRINT: ")
p(novos_produtos_com_filter)


# -----------------------------------------------
print()

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista_com_comprehension = [(x, y) 
                           for x in range(3) 
                           for y in range(3)
                        ]

print(lista)
print() 
print(lista_com_comprehension)