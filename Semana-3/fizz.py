# Semana 3 - Exercício 2 - Imprime fizz se número divisível por 3

numero = int(input("Digite um número inteiro: "))

resto = numero % 3

if (resto == 0):
	print("Fizz")
else:
	print(numero)