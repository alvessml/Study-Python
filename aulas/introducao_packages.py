from sys import path

from introducao_packages_folder.modulo import soma 
import introducao_packages_folder.modulo
from introducao_packages_folder import modulo 

# print(*path, sep='\n') # *path (path é uma lista, ou seja, * desempacota a lista)

print(soma(5, 3))
print(introducao_packages_folder.modulo.soma(8, 4))
print(modulo.soma(3, 7))


# from introducao_packages_folder.modulo import * 
# print(soma(3, 4))