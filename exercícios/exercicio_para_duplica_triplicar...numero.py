def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar 

quadruplicar = criar_multiplicador(4)

print(quadruplicar(2))