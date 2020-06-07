def fizzbuzz(numero):
	resto3 = numero % 3
	resto5 = numero % 5

	if ( (resto3 == 0) and (resto5 != 0) ):
		mensagem = 'Fizz'
		return mensagem
	if ( (resto3 != 0) and (resto5 == 0) ):
		mensagem = 'Buzz'
		return mensagem
	if ( (resto3 == 0) and (resto5 == 0) ):
		mensagem = 'FizzBuzz'
		return mensagem
	else:
		return numero

