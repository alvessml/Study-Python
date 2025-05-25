"""
Introdução ao try/except/else/finally e Raise

try -> tentar executar o código
except -> ocorre algum erro ao tentar executar
"""

# -----------------------------------------------------------------------------------------

# Link da HIERARQUIA de exceções
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# -----------------------------------------------------------------------------------------

# USANDO O TRY + EXCEPT

# numero_str = input('Vou dobrar o número que você digitar: ')

# try:
#     # Tenta converter a entrada para float
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# except:
#     # Lida com o erro caso a entrada não seja um número válido
#     print('Erro: Isso não é um número válido.')

try:
    a = 2
    b = 1
    # print(b[0]) # Ocorre erro de TypeError
    print('Linha 1'[1000])
    c = a/b 
    print('Linha 2')

    
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
# except (TypeError, IndexError): # Adcionando mais de uma Classe de erro na linha
#    print('TypeError')       
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome do erro: ', error.__class__.__name__)
except Exception: # Maior clase de Erros (generaliza)
    print('Erro Desconhecido')
print('Continuar')


print()
print()

# USANDO O TRY + FINALLY
# Finally sempre será executado

try: 
    print('ABRIR ARQUIVO')
finally:
    print('FECHAR ARQUIVO')

print()


# Tratar erro, depois finalizar
try: 
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('Dividiu zero')
finally:
    print('FECHAR ARQUIVO')


print()
print()

# USANDO TRY + ELSE
# Print informa que não deu erro
try: 
    print('ABRIR ARQUIVO')
    8/1
except ZeroDivisionError:
    print('Dividiu zero')
else: 
    print('Não houve erro')
finally:
    print('FECHAR ARQUIVO')



print()
print()

# RAISE

# print(123)
# raise ValueError('Deu erro') # Lançando um erro qualquer
# print(456)

print('CÓDIGO PARA EXPLAICAR RAISE: ')
# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))