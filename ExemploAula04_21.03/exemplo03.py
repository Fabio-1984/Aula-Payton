'''Vamos criar um programa solicite um número real,
   Calcule e apresente:
   a) Valor absoluto;
   b) Somente sua parte inteira;
   c Sua raiz quadrada;
   d) O fatorial desse número
   '''

import math

num = float(input("Digite um número: "))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.trunc(math.fabs(inteiro)))

print("Valor Absoluto: ", absoluto, "\nInteiro: ", inteiro, "\nRaiz: ", raiz, "\nFatorial: ", fatorial )