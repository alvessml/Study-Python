# Desempacotamento 
#     empacota em resto
x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto)

# args = Argumentos não nomeados
 
def soma(*args):
    total = 0
    for num in args:
        total += num
    print(total)
 
soma(1, 3, 5, 7, 9)  