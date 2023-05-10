#Situação Problema

#Faça um programa em Python que leia os doze salários recebidos por um funcionário durante um ano, calcule e exiba na tela quanto ele receberá de 13 salário e 1/3 de férias. Para os cálculos, utilize as seguintes definições:

# O 13 salário deverá ser igual á média dos salários recebidos no ano
# Para o cálculo de 1/3 de férias, faça a média dos salários * 1/3

# Obs.:
   # 1 - Obrigatório utilizar alguma estrutura de repetição
   # 2 - Identificar o mês(Ex: Qual o salário recebido em Jan: R$)



meses = ["Jan", "Fev", "Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
salarios = []
soma = 0


for i in range(12):
    sal = float(input("Qual o salário de %s R$ " %(meses[i])))
    salarios.append(sal)
    soma = soma + salarios[i]


    media = soma/len(meses)
    print("13 salário R$ ", media)
    ferias = media * 1/3
    print("Férias R$ ", ferias)



 