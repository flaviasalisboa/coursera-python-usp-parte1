# Semana 7 - Exercício 1 - Imprime retângulo cheio
# com os caracteres #####

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

i = 1
while i <= altura:
	j = 1
	while j <= largura:
		print("#", end = "")
		j = j + 1
	i = i + 1
	print()