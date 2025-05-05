cpf = input('Digite o CPF (***.***.***-**): ')
cpf_sem_pontos = cpf.replace('.', '').replace('-', '')
cpf_9_digitos = cpf_sem_pontos[:9]

cont_regressivo = 10
result_digito_1 = 0
for i in cpf_9_digitos:
    result_digito_1 += int(i) * cont_regressivo
    cont_regressivo -= 1

digito_1 = (result_digito_1 * 10) % 11
digito_1 = 0 if digito_1 > 9 else digito_1

cpf_10_digitos = cpf_9_digitos + str(digito_1)

cont_regressivo = 11
result_digito_2 = 0
for j in cpf_10_digitos:
    result_digito_2 += int(j) * cont_regressivo
    cont_regressivo -= 1

digito_2 = (result_digito_2 * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2

cpf_11_digitos_gerado = cpf_10_digitos + str(digito_2)

# Adiciona os pontos na string cpf_9_digitos + digito 1 e 2 + Depois confirma se o CPF é válido ou não
#Obs: Relizei o caminho mais difícil para organizar a variável contendo o cpf com pontos de 9 dígitos
s = cpf_9_digitos[::-1]
partes = [s[i:i+3] for i in range(0, len(s), 3)]
cpf_9_digitos_com_pontos = '.'.join(partes)[::-1]

t = str(digito_1) + str(digito_2)
t = t[::-1]
partes = [t[i:i+1] for i in range(0, len(t))]
partes.append("-")
cpf_gerado = cpf_9_digitos_com_pontos + ''.join(partes)[::-1]

if cpf_gerado == cpf:
    print(f"{cpf_gerado} é válido!")
else:
    print(f"{cpf_gerado} NÃO é válido.")