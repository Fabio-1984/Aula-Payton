### Vamos criar um programa que solicite ao usuário
### um número inteiro com trÊs dígitos e exiba esse
### número com os dígitos invertidos. ###

num = int(input("Digite um número inteiro: "))
d1 = num // 100 # Parte inteira da divisão
d2 = num % 100 // 10 #% resto da divisão
d3 = num % 10
invertido = d3 * 100 + d2 * 10 + d1


print("Resultado: ", invertido)