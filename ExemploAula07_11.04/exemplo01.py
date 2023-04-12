# 1 - Escreva um algoritimo que solicite ao usuário a média de um aluno e o percentual de
# frequencia e mostre a sua situação, conforme a tabela abaixo:



media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequencia: "))

if frequencia < 75:
    print(" Reprovado por falta!")
elif media < 6:
    print("reprovado por nota")
else:
    print("Aprovado = Férias")    