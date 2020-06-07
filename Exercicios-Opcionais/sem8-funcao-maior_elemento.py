def maior_elemento(lista):
	maior = lista[0]
	i = 1
	while i < len(lista):
		if lista[i] > maior:
			maior = lista[i]
		i = i + 1
	return maior
