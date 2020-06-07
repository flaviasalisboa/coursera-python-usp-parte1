largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# cabecalho
j = 1
while j <= largura:
	print("#", end = "")
	j = j + 1
print()
# meio sem preenchimento
i = 1
while i <= altura-2:
	j = 1
	while j <= largura:
		if (j == 1) or (j == largura): 
			print("#", end = "")
		else:
			print(" ", end = "")
		j = j + 1
	i = i + 1
	print()
# rodape
j = 1
while j <= largura:
	print("#", end = "")
	j = j + 1
print()