import random

def gerar_aleatorio(tam):
    vetor = []
    for i in range(tam):
        vetor.append(random.randint(0,100))
    return vetor

def gerar_ordenado(tam):
    vetor = sorted(gerar_aleatorio(tam))
    return vetor

def gerar_decrescente(tam):
    vetor = sorted(gerar_aleatorio(tam),reverse=True)
    return vetor

