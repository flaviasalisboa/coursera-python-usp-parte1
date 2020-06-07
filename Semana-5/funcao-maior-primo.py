def ePrimo(k):
	e_primo = True
	# procura um divisor de n entre 2 e n-1
	divisor = 2
	while divisor < k and e_primo:
		if k % divisor == 0:
			e_primo = False
		divisor = divisor + 1
	return e_primo

def maior_primo(n):
	i = 1
	while i <= n:
		if ePrimo(i) == True:
			primo = i
		i = i + 1
	return primo
	
