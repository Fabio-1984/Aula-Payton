# 5-Elabore um algoritmo que obtenha o salário base e o tempo de serviço de um
# funcionário, calcule e mostre o salário acrescido da gratificação, conforme a tabela a
# seguir:

#         Salário Base         Tempo de serviço           Gratificação

#     Superior a R$1500,00        Até 3 anos                R$200,00
#                              Maior de 3 anos              R$300,00
#
#      Até R$1500,00              Até 3 anos                R$230,00
#                              Entre 3 e 6 anos             R$330,00   
#                              Mais de 6 anos               R$350,00



#


salario = float(input("Digite o valor do salário base: "))
tempoServico = float(input("Digite o tempo de serviço "))

if salario > 1500.00 and tempoServico == 3:
    gratificacao = 200.00
    print("O valor da gratificação é: ", gratificacao, "Valor total a receber é: ", salario + gratificacao)
