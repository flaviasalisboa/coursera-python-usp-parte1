numero = int(input("Digite um numero inteiro: "))

resto3 = numero % 3
resto5 = numero % 5

if ( (resto3 == 0) and (resto5 == 0) ):
	print("FizzBuzz")
else:
	print(numero)