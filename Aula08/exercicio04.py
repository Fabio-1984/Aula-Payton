# 4- Elabore um programa em Python que implemente uma calculadora com as funções de
# somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
# valores, e perguntar qual a operação pretendida (‘+’, ‘-‘,‘*’ ou ‘/’ ) e a seguir calcular e
# mostrar o resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação pretendida (‘+’, ‘-‘,‘*’ ou ‘/’ ): ")

if operacao == "+":
    print("A soma dos números é: ", num1 + num2)
elif operacao == "-":
    print("A subtração dos números é: ", num1 - num2)
elif operacao == "*":
    print("A multiplicação dos números é: ", num1 * num2)
elif operacao == "/":
    print("A mudivisão dos números é: ", num1 / num2)
else:
    print("Operação inválida")
