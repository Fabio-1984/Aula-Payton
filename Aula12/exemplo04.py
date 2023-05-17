#strip - retira a quebra de linha e o espaço em branco antes e depois


b = "\n Fizeram a atividade? "
b = b.strip()
print(b)

#Operador in - verifica se uma substring está contida na string

print("idade" in b)


#função find - retorna onde a substring começa na string

print(b.find("Fiz"))

#replace - substitui todas as ocorrências de uma substring

b = b.replace("Atividade", "Avaliação")

print(b)


#upper - converte o texto para maiúsculo
print(b.upper())
#lower - converte o texto para minúsculo
print(b.lower())

#split - separa a string

separado = b.split("a")

print(separado)
