# Semana 4 - Exercício 1 - Fatorial de um número n
# n! = n * (n-1) * (n-2) até o 1.

numero = int(input("Digite o valor de n: "))

resultado = 1
count = 1

while count <= numero:
    resultado = resultado * count
    count = count + 1

print(resultado)