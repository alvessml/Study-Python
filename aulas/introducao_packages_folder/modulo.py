# Para importa somente uma variável ou function se o usuário import * (ou seja, tudo do meu modulo)
__all__ = [
    'variavel', 'soma'
]

variavel = 'Alguma coisa'

def soma(x, y):
    return x + y