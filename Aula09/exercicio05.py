# Faça um programa que calcula e mostre a média de uma quantidade indeterminada de números inteiros digitados pelo usuário. use a estrutura de repetição enquanto(while).


#Laço condicional (Indeterminado)

#Contador
contador = 0
#Acumulador
soma = 0
#Inicialização da variével de controle
resp = 'S'


while resp == 'S' or resp == 's':
    n = int(input("Digite em número: "))
    contador = contador + 1
    soma = soma + n #acumula
    #Atualiza a variável de controle
    resp = input("Deseja digitar outro numero? (S/N)")

    media = soma/contador
    print("A média é: ", media)