# 3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:

#     Valor de compra                   Valor de venda
#     valor < R$10,00                   lucro de 70%
#  R$ 10,00 <= valor < R$ 30,00         lucro de 50%
#  R$ 30,00 <= valor < R$ 50,00         lucro de 40%
#     valor >= R$50,00                  lucro de 30%

# Crie uma programa que permita digitar o nome do produto e valor da compra, e imprime
#o nome do produto e o valor da venda.

produto = input("Digite o produto: ")
valor = float(input("Digite o valor da compra: "))


if valor < 10.00:
    lucro = 70/100
    print("Nome do produto: ", produto, "Total a pagar: ", valor * lucro + valor, "Lucro", lucro * valor)
elif valor >= 10.00 and valor < 30.00:
    lucro = 50/100
    print("Nome do produto: ", produto, "Total a pagar: ", valor * lucro + valor, "Lucro", lucro * valor)
elif valor >= 30.00 and valor < 50.00:
    lucro = 40/100
    print("Nome do produto: ", produto, "Total a pagar: ", valor * lucro + valor, "Lucro", lucro * valor)
elif valor >= 50.00:
    lucro = 30/100
    print("Nome do produto: ", produto, "Total a pagar: ", valor * lucro + valor, "Lucro", lucro * valor)
else:
    print("Inválido")

