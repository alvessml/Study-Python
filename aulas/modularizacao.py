# Todo primeiro módulo executado se chama __main__
# print('Este módulo se chama', __name__) # usando o __name__ para chamar 

# importando módulo:
# Obs: o módulo que você quer importar, tem que estar na mesma pasta do
# módulo onde você vai chamar.

# import modularizacao_m
# import sys

# print('Este módulo se chama', __name__) # Ele executa o módulo que chamei primeiro, haja vista que, lá possui um print sys. E depois esse módulo principal (__main__)
# print(*sys.path, sep='\n')

#____________________________________________________________________________
try: 
    import sys
    sys.path.append('/home/samuel/Documents/teste_python/')
    import modulo_teste
except ModuleNotFoundError:
    print('Erro. Módulo chamado NÃO foi encontrado.')
