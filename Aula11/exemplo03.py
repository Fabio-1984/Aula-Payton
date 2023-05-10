#Média de uma quantidade indeterminada de valores
#Critério de parada é número = 0

soma = 0 #acumulador
numeros = list() #Cria a lista numeros

while True: #Enquanto for verdadeiro
    num = int(input("Digite um número: "))
    if num == 0: #Critério de parada da repetição
       break # para a estrutura de repetição

    numeros.append(num)
    soma = soma + num

    media = soma/len(numeros)

    print("A média dos valores digitados: ", media)
    print(numeros)