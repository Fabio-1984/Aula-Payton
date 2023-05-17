# for atuando sobre a string


string = input("Digite em texto: ")
inverso = ""

for x in string:

    inverso = x + inverso

print(inverso)   


#Palindrome = normal ingual o inverso

if inverso == string:
    print("É palindrome")
else:
    print("Não é paíndrome")
    
        