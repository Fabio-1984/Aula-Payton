#Exemplo 02 - Aula 03


#Entrada
#IMC = peso/(altura*altura)

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#Processamento

imc = round(peso/altura**2, 2) #imc = peso/(altura*altura)

#Saida


print("O seu imc é: ", imc)

