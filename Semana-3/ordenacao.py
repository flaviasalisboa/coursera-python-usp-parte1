a = int(input("Digite o primeiro numero inteiro: "))
b = int(input("Digite o segundo numero inteiro: "))
c = int(input("Digite o terceiro numero inteiro: "))

if ( (a<b) and (a<c) and (b<c) ):
	print("crescente")
else:
	print("não está em ordem crescente")