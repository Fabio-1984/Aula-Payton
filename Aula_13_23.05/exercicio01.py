# 1 - Faça um programa em Python que solicite a uma quantidade
# indeterminada de usuários sua altura e peso, calcule e imprima para
# cada um o seu IMC. Sabendo que: IMC = peso/altura2


resp = 'S'


while resp.upper() == 'S':  
  
     altura = float(input("Digite a sua altura: "))
     peso = float(input("Digite o seu peso: "))

     print('IMC = %.2f' %(peso/altura**2))

     print("Deseja continuar? S para sim ou N para não")

    

    
 
   



