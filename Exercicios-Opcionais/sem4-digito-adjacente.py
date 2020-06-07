
numero = int(input("Digite um numero inteiro: "))

num1 = numero
resto1 = numero % 10

while (numero // 10) != 0:
	numero = numero // 10
	resto = numero % 10
	if resto == resto1:
		print("sim")
		numero = num1
		break
	resto1 = resto

if (numero // 10) == 0:
        print("nao")





