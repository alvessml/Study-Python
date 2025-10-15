"""
=====Métodos de Strings=====

Python fornece vários métodos integrados para trabalhar com strings. Alguns dos métodos mais comuns incluem:

    lower(): Converte todos os caracteres da string para minúsculas.

    upper(): Converte todos os caracteres da string para maiúsculas.

    replace(old, new): Substitui todas as ocorrências de old por new.

    split(delimiter): Divide a string em uma lista de substrings, utilizando o delimitador especificado.

    strip(): Remove os espaços em branco no início e no final da string.
EX:
string = " Python é Incrível "
print(string.lower())  # Resultado: ' python é incrível '
print(string.upper())  # Resultado: ' PYTHON É INCRÍVEL '
print(string.replace("Incrível", "genial"))  # Resultado: ' Python é genial '
print(string.split())  # Resultado: ['Python', 'é', 'Incrível']
print(string.strip())  # Resultado: 'Python é Incrível'


=====Concatenação de Strings=====
A concatenação de strings implica unir duas ou mais strings em uma só. Isso pode ser feito utilizando o operador + ou o método join().
EX:
string1 = "Python"
string2 = "é genial"
resultado = string1 + " " + string2
print(resultado)  # Resultado: 'Python é genial'
partes = ["Python", "é", "genial"]
resultado = " ".join(partes)
print(resultado)  # Resultado: 'Python é genial'


=====Números=====

Os números em Python são divididos em vários tipos:

    Inteiros (int): São números sem parte decimal, tanto positivos quanto negativos.

    Reais (float): São números com decimais.

    Complexos (complex): São números que incluem uma parte real e uma imaginária.

As operações básicas que podem ser realizadas com números incluem:

    Soma (+): Adição de dois números.

    Subtração (-): Subtração de um número de outro.

    Multiplicação (*): Produto de dois números.

    Divisão (/): Quociente de dois números.

    Divisão inteira (//): Quociente inteiro da divisão de dois números.

    Módulo (%): Resto da divisão de dois números.

    Potenciação (): Um número elevado à potência de outro.
"""

string = "samuel"

print(string[1::3])