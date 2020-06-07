# Semana 3 - Exercício 5 - Verifica a ordenação
# dos números - crescente ou não

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if ( (a<b) and (a<c) and (b<c) ):
	print("crescente")
else:
	print("não está em ordem crescente")