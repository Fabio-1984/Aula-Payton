


peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))


imc = peso/(altura*altura)


if imc< 20:
    print("Você esta abaixo do peso: ")
elif imc >= 20 and imc < 25:
    print("Seu peso esta normal")
elif imc >= 25 and imc < 30:
    print("Você esta com sobre peso")
elif imc >= 30 and imc < 40:
    print("Você esta obeso")
else:
    print("Você é um obeso morbido")    

