
#Exercicio calculo da base da pirâmide

piramide = float(input("Digite o valor da altura do troco da piramide: "))
bmenor = float(input("Digite o valor da Base menor: "))
bmaior = float(input("Digite o valor da Base maior: "))

volume = piramide/3*(bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)

print("O valor do tronco da pirâmide é: ", volume)