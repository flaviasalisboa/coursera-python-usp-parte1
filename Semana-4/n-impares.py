# Semana 4 - Exercício 2 - Imprime os números primos
# até o valor de n dado (primos de 1 a n) 

numero = int(input("Digite o valor de n: "))

cont = 1
impar = 1

while cont <= numero:
	print(impar)
	impar = impar + 2
	cont = cont + 1