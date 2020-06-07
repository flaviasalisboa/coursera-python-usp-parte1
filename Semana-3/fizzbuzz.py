# Semana 3 - Exercício 4 - Imprime FizzBuzz se número 
# divisível por 3 e por 5

numero = int(input("Digite um número inteiro: "))

resto3 = numero % 3
resto5 = numero % 5

if ( (resto3 == 0) and (resto5 == 0) ):
	print("FizzBuzz")
else:
	print(numero)