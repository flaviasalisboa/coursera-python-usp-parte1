n = int(input("Digite um número:"))
lista = []
while n > 0:
	lista.append(n)
	n = int(input("Digite um número:"))
tam = len(lista)
inv = tam - 1

while inv >= 0:
	print(lista[inv]) 
	inv = inv - 1