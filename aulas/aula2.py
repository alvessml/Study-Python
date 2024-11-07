# Argumento não nomeado
print(12, 34)
print(56, 78)


# Argumento nomeado
print(12, 34, sep="-")
print(56, 78, sep='-')

print(56, 78, sep="-", end="\r\n") # Não muda nada pois \r\n é padrão no windows
print(56, 78, sep="-", end="\n#") 


