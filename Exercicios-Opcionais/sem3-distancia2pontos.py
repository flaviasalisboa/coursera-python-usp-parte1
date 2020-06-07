import math

x1 = float(input("Digite o x do primeiro ponto (x,y): "))
y1 = float(input("Digite o y do primeiro ponto (x,y): "))
x2 = float(input("Digite o x do segundo ponto (x,y): "))
y2 = float(input("Digite o y do segundo ponto (x,y): "))

raiz = ( (x1-x2)**2 + (y1-y2)**2 )
distancia = math.sqrt(raiz)

if ( distancia >= 10 ):
	print("longe")
else:
	print("perto")