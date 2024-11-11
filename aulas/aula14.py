# Objetos e métodos

# Objetos - pode fazer algumas ações e essas ações são chamados de métodos

# Uso do método format
a = 'AAAAA'

b = 'BBBBB'

c = 1.1

# string = 'a={0} b={1} c={2:.2f}'
# string = 'a={1} b={0} c={2:.2f}'
string = 'a={nome1} b={nome2} c={nome3:.2f}'

                        # Parametro nomeado
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)