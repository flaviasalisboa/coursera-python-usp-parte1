
def ePrimo(k):
	e_primo = True
	# procura um divisor de n entre 2 e n-1
	divisor = 2
	while divisor < k and e_primo:
		if k % divisor == 0:
			e_primo = False
		divisor = divisor + 1
	return e_primo

def n_primos(n):
	limite = 2
	soma = 0
	while limite <= n:
		if ePrimo(limite):
			soma = soma + 1
		limite = limite + 1
	return soma
	
