string = 'Samuel'

# Atributos: são nomes que estão definidos dentro da string 
# Métodos: ações 

if hasattr(string, 'upper'): # Diz: Existe o método upper aqui?
    print('Existe upper')
    print(string.upper()) # então ele aplica o método


metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # o getattr executa o metodo que foi definido dinamicamente.