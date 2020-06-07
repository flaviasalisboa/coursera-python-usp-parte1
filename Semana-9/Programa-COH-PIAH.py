# TAREFA DE PROGRAMAÇÃO - SEMANA 9 - PROGRAMA COMPLETO COH-PIAH
# COURSERA - USP - CIÊNCIA DA COMPUTAÇÃO COM PYTHON PARTE 1
# AUTOR: FLÁVIA LISBOA - DATA: JUNHO/2020

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

# CRIADA E IMPLEMENTADA POR: Flávia Lisboa para uso na função calcula_assinatura 
# Retorna quantidade de caracteres de um conjunto de palavras, frases, sentenças
def quantCaracteres(palavraFraseSentenca):
    qtdCaracteres = 0

    for caracter in palavraFraseSentenca:
        qtdCaracteres = qtdCaracteres + len(caracter)

    return qtdCaracteres

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# IMPLEMENTADA POR: Flávia Lisboa  
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatorio = 0

    for i in range(0,6): 
        somatorio = somatorio + (abs(as_a[i] - as_b[i]))
        
    grauSimilaridade = somatorio / 6
    return round(grauSimilaridade, 2)

# IMPLEMENTADA POR: Flávia Lisboa  
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    frases = []
    palavras = []
    
    # separa e calcula total de sentencas do texto
    sentencas = separa_sentencas(texto)
    totalSentencas = len(sentencas)
    
    # separa e calcula total de frases do texto
    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    totalFrases = len(frases)

    #separa e calcula total de palavras do texto
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    totalPalavras = len(palavras)

    # 1) Tamanho médio de palavras e somatório do tamanho das palavras
    #numCaracteres = 0
    #for cadaPalavra in palavras:
    #    numCaracteres = numCaracteres + len(cadaPalavra)

    tamanhoMedioPalavra = quantCaracteres(palavras) / totalPalavras
    
    # 2) Relação Type-Token
    typeToken = n_palavras_diferentes(palavras) / totalPalavras

    # 3) Razão Hapax Legomana
    hapaxLegomana = n_palavras_unicas(palavras) / totalPalavras

    # 4) Tamanho médio de sentença
    tamanhoMedioSentenca = quantCaracteres(sentencas) / totalSentencas
    
    # 5) Complexidade de sentença
    complexidadeSentenca = totalFrases / totalSentencas
    
    # 6) Tamanho médio da frase
    tamanhoMedioFrase = quantCaracteres(frases) / totalFrases

    assinatura = [tamanhoMedioPalavra, typeToken, hapaxLegomana, tamanhoMedioSentenca, complexidadeSentenca, tamanhoMedioFrase]
    print(assinatura)
    return assinatura

# IMPLEMENTADA POR: Flávia Lisboa  
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    comparacoes = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(assinatura, ass_cp)
        comparacoes.append(comparacao)

    menorComparacao = min(comparacoes)
    indiceMenorComparacao = (comparacoes.index(menorComparacao) + 1)
              
    print ("O autor do texto", indiceMenorComparacao, "está infectado com COH-PIAH.")
    return indiceMenorComparacao

def main():
    assinaturaCopia = le_assinatura()
    textosDigitados = le_textos()
    avalia_textos(textosDigitados, assinaturaCopia)

main()
