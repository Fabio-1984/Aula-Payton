#Funções remove

#Cria a lista nomes

nomes = []

#append adiciona o valor no final da lista

for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n)

#Exibe valores aa lista

print(nomes)

#Remove - exclui da lista o item especificado

exclue = input("Digite o nome a ser excluido: ")
nomes.remove(exclue)

print(nomes)

#Enumerate - Tuplas são similares às listas, porém são imutáveis

for x, e in enumerate(nomes):
   #print("[%d] - %s" %(x+1, e))
    print(x+1, " - ", e)
