

codDiaria = input(" Digite o tipo de hospedagem \nS - Simples \nD - Dupla \nT - Tripla: ")
qtDiaria = int(input(" Digite a quantidade de diárias: "))

if codDiaria == "S" or "s":
    print("Tipo de quarto simples, ", "Total a pagar: ", qtDiaria * 255.50)
elif codDiaria == "D" or "d":
    print("Tipo de quarto Duplo", "Total a pagar: ", qtDiaria * 305.50)    
elif codDiaria == "T" or "t":
    print("Tipo de quarto Triplo", "Total a pagar: ", qtDiaria * 360.50)     
else:
    print("Tipo de diária inválido")    