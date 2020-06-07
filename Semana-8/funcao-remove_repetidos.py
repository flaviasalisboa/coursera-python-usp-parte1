# Semana 8 - Exercício 1 - Função remove_repetidos
# de uma lista retira os valores repetidos

def remove_repetidos(lista):
	templista = []
	for i in lista:
		if i not in templista:
			templista.append(i)
	templista.sort()
	return templista


