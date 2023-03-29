#Exemplo 04 - média


#Entrada de dados

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))


#Processamento

m = (n1 + n2)/2

if m >= 6:  #Bloco verdadeiro
    print('Aprovdo, a sua média é: %.2f'%m)

else:  #Bloco falso
    print('Reprovado, a sua média é: %.2f'%m)
