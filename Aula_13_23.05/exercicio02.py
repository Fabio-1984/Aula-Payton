# 2 - Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados
# de idade e salário. Faça um algoritmo que informe:
# a) a média de idade do grupo;
# b) a média de salários das pessoas com mais de 40 anos;

# Encerre a entrada de dados quando for digitada uma idade negativa (os dados da idade
# negativa não podem entrar nos cálculos dos itens solicitados acima).


#acumuladores
somaId = 0
somaSal = 0

#contadores
contId = 0
contSal = 0

while True:
    idade = int(input('Digite a idade '))
    if idade < 0:
        break #parar o while
    salario = float(input('Digite o salario: '))
    somaId += idade # somaId = somaId + idade
    contId += 1 # contId = contId + 1

    if idade > 40:
        somaSal += salario
        contSal += 1

# termina o while
if somaId > 0: 
    mediaId = somaId/contId

if somaSal > 0:
    mediaSal = somaSal/contSal
    print('Média dos salários: ',mediaSal)



