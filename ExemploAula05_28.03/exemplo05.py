#Exemplo 05 - Raiz quadrada


import math

num = float(input('Dígite um número: '))

if num > 0:
    raiz = math.sqrt(num)
    print("O valor da raiz quadrada é: ", raiz)

else:
    print("Não é possível calcular a raiz")