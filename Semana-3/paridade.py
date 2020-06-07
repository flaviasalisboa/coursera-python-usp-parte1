# Semana 3 - Exercício 1 - Número par ou ímpar

numero = int(input("Digite um número inteiro: "))

resto = numero % 2

if (resto == 0):
	print("par")
else:
	print("ímpar")