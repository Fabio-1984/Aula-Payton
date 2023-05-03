#3 Faça um programa que calcule e mostre a média entre 10 alunos, Use a estrutura de repetição enquanto(while).

# Laço contato com while

#Contador
contador = 1 # Inicialização da variável de controle (contador)

while contador == 5:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda  nota: "))
    media = (n1 + n2)/2
    print("A média é: ", media)
    #Atualizaçã da variável controle

    contador = contador + 1