# Semana 3 - Exercício 3 - Imprime buzz se número divisível por 5

numero = int(input("Digite um número inteiro: "))

resto = numero % 5

if (resto == 0):
	print("Buzz")
else:
	print(numero)