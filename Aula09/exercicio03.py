# 2 - Faça um algoritimo que solicite ao usuário 10 números reais, cacule e mostre a soma dos números digitados. Use a estrutura de repetição for.


#Acumulador
soma = 0

for i in range(10):
    n = float(input("Digite um número real: "))
    #Acumula o valor digitado = somatória
    soma = soma + n
    print(i, "A soma dos valores digitados é: ", soma)