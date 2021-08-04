valor = input('Insira um valor')

if(valor.isascii()):
        print('Valor ascii')
elif(valor.isalnum()):
        print('Valor numérico')
elif(valor.isalpha()):
        print('Valor alfanumérico')
elif(valor.isdecimal()):
        print('Valor decimal')