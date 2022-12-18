from utils import *


def resolve(estado, listaPassos):

    estado = list(estado)

    for passo in listaPassos:
        for i in range(len(estado)):
            if estado[i] == '_':
                break

        if passo == "direita":
            estado[i], estado[i+1] = estado[i+1], estado[i]
        elif passo == "esquerda":
            estado[i], estado[i-1] = estado[i-1], estado[i]
        elif passo == "acima":
            estado[i], estado[i-3] = estado[i-3], estado[i]
        elif passo == "abaixo":
            estado[i], estado[i+3] = estado[i+3], estado[i]

    return "".join(estado)