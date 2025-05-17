def saudacoes(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = saudacoes('Bom dia')

print(falar_bom_dia('Samuel'))