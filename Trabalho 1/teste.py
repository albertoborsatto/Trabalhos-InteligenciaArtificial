from utils import *

def resolve(estado, listaPassos):

    for i in range(len(estado)):
        if estado[i] == '_':
            break

    for passo in range(len(listaPassos)):
        if passo == "direita":
            estado[i], estado[i+1] = estado[i+1], estado[i]
        elif passo == "esquerda":
            estado[i], estado[i-1] = estado[i-1], estado[i]
        elif passo == "cima":
            estado[i], estado[i-3] = estado[i-3], estado[i]
        elif passo == "abaixo":
            estado[i], estado[i+3] = estado[i+3], estado[i]

    return estado
