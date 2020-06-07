# TAREFA DE PROGRAMAÇÃO - SEMANA 6 - JOGO DO NIM
# COURSERA - USP - CIÊNCIA DA COMPUTAÇÃO COM PYTHON PARTE 1
# AUTOR: FLÁVIA LISBOA - DATA: JUNHO/2020

def computador_escolhe_jogada(n, m):
    computadorTira = 1
    mMais1 = m+1
    while (computadorTira <= m):
        if (n - computadorTira) % (mMais1) == 0:
            return computadorTira
        else:
            computadorTira = computadorTira + 1

    return computadorTira

def usuario_escolhe_jogada(n, m):
	jogadaValida = False

	while (not jogadaValida):
		jogadorTira = int(input("Quantas peças você vai tirar? "))
		if (jogadorTira < 1) or (jogadorTira > m):
			print()
			print("Oops! Jogada inválida! Tente de novo.")
			print()
		else:
			jogadaValida = True
	return jogadorTira

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	print()
	mMais1 = m + 1
	
	computadorJoga = False

	if (n % mMais1 == 0):
		print("Você começa!")
		print()
	else:
		print("Computador começa!")
		computadorJoga = True

	while (n >= 1):
		if (computadorJoga): # jogador: Computador
			# volta quantas pecas o computador tirou
			jogadaComp = computador_escolhe_jogada(n, m)
			n = n - jogadaComp
			if (jogadaComp == 1):
				print("O computador tirou uma peça.")
			else:
				print("O computador tirou", jogadaComp, "peças.")
			computadorJoga = False
		else: # jogador: Usuario
			# volta quantas pecas o usuario tirou
			jogadaUser = usuario_escolhe_jogada(n, m)
			n = n - jogadaUser
			if (jogadaUser == 1):
				print()
				print("Você tirou uma peça.")
			else:
				print()
				print("Voce tirou", jogadaUser, "peças.")
			computadorJoga = True

		if (n == 1):
			print("Agora resta apenas uma peça no tabuleiro")
			print()
		else:
			if (n != 0):
				print("Agora restam", n, "peças no tabuleiro.")
				print()

	print("Fim do jogo! O computador ganhou!")

def campeonato():
    rodada = 1
    while (rodada <= 3):
        print()
        print("**** Rodada", rodada, "****")
        print()
        partida()
        rodada = rodada + 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")


# Inicio do Jogo do NIM - acima estao todas as funcoes usadas no programa    
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha = int(input(""))
	
if (escolha != 1 and escolha != 2):
	print("Você só deve escolher 1 ou 2")
	escolha = int(input(""))
if (escolha == 1):
	print("Voce escolheu uma partida isolada!")
	print()
	partida()
if (escolha == 2):
	print("Voce escolheu um campeonato!")
	print()
	campeonato()

