#Exemplo 03 - Par ou Impar

nro = int(input('Digite um número: '))

resto = nro % 2 #Resto da divisão

if resto == 0:
    print('Par')
else:
    print('Impar')    