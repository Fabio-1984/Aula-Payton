# Função insert(i, valor)

itens = []

for i in range(5):
    item = input("Digite o item que deseja comprar: ")

    itens.insert(i, item) #Insere o item no indice i
    itens.sort() #Coloca os itens em ordem

print("Itens do compra: ", itens) 
itens.insert(2, "Pão")
itens.append("Bolacha")  

print(itens)