# 3- Faça um programa em Python que contenha 3 listas, uma com as notas, a segunda
# com nomes dos alunos e a terceira com nome da disciplina. Utilize como critério de
# parada a nota negativa.
# § Calcule e mostre a média das notas.
# § Exiba o nome do aluno e a disciplina, as quais a nota é maior do que média
# É obrigatório o uso de estrutura de repetição e listas.


nomes = []
notas = []
disc = []

soma = 0


while True:
    nota = float(input("Digite a nota: "))

    if nota < 0:
        break
    notas.append(nota)
    soma += nota
   
    nomes.append(input("Digite o nome: "))

    

    d = input("Digite o nome da disciplina: ")

    disc.append(d)


    media = soma/len(notas)

    for i in range(len(notas)):
        if notas[i]> media:
            print('Nome do aluno: ', nomes[i], 
                  '\Disciplina', disc[i], 
                  '\nNota', notas[i])


