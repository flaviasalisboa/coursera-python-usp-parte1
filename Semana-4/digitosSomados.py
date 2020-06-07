numero = int(input("Digite um numero inteiro: "))
soma = 0

while ( numero != 0):
	resto = numero % 10
	soma = soma + resto
	numero = numero // 10

print(soma)
#print("A soma dos digitos desse numero e", soma)