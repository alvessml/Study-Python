hora_usr = input('Digite uma hora qualquer entre (00 á 23): ')

try:
    hora_usr_number = int(hora_usr)
    if hora_usr_number >= 0 and hora_usr_number <= 11:
        print('Bom dia')
    elif hora_usr_number >= 12 and hora_usr_number <= 17:
        print('Boa tarde')
    elif hora_usr_number >= 18 and hora_usr_number<= 23:
        print('Boa noite')
    else: 
        print('Não reconheço essa hora!') 
except: 
    print('Digite somente números inteiros!')