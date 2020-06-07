def remove_repetidos(lista):
	templista = []
	for i in lista:
		if i not in templista:
			templista.append(i)
	templista.sort()
	return templista


