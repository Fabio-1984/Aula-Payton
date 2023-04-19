# 1 - Criar um algoritmo que solicite ao usuário o valor total da compra e a quantidade de
# parcelas a financiar e o sistema deve imprimir o valor de cada parcela de acordo com os
# juros da tabela abaixo:

valorTotal = float(input("Digite o valor total da compra: "))
totalParcelas = int(input("Digite a quantidade de parcelas: "))


if totalParcelas == 2:
    juros = 3/100
    print("O valor total da parcela é: ", valorTotal * juros + valorTotal, "Valor o juros aplicado: ", juros )
elif totalParcelas == 4:
    juros = 7/100
    print("O valor total da parcela é: ",  valorTotal * juros + valorTotal, "Valor o juros aplicado: ", juros)
elif totalParcelas == 6:
    juros = 9/100
    print("O valor total da parcela é: ", valorTotal * juros + valorTotal, "Valor o juros aplicado: ", juros)
elif totalParcelas == 8:
    juros = 12/100
    print("O valor total da parcela é: ", valorTotal * juros + valorTotal, "Valor o juros aplicado: ", juros)    
else:
    print("Inválido")   