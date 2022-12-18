from utils import *
from collections import deque
from teste import *
from heapq import *
from queue import PriorityQueue

def resolve(estado, listaPassos):

    estado = list(estado)

    for passo in listaPassos:
        for i in range(len(estado)):
            if estado[i] == '_':
                break
        #print(passo)
        #print(estado)
        #print(i)
        if passo == "direita":
            estado[i], estado[i+1] = estado[i+1], estado[i]
        elif passo == "esquerda":
            estado[i], estado[i-1] = estado[i-1], estado[i]
        elif passo == "acima":
            estado[i], estado[i-3] = estado[i-3], estado[i]
        elif passo == "abaixo":
            estado[i], estado[i+3] = estado[i+3], estado[i]

        #print(estado, end="\n\n")

        

    return "".join(estado)


class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


def sucessor(string):
    lista = []

    matriz = stringToMatrix3x3(string)
    #print(matriz)

    sair = False
    #Encontra a posição do espaço vazio _
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == '_':
                sair = True
                break
        if sair:
            break

    if (i < 2):
        tupla = ("abaixo", swap(string, 3*i+j, 3*(i+1)+j))
        lista.append(tupla)

    if (i > 0):
        tupla = ("acima", swap(string, 3*i+j, 3*(i-1)+j))
        lista.append(tupla)

    if (j < 2):
        tupla = ("direita", swap(string, 3*i+j, 3*i + j+1))
        lista.append(tupla)

    if (j > 0):
        tupla = ("esquerda", swap(string, 3*i+j, 3*i + j-1))
        lista.append(tupla)
    
    #print(lista, end= '\n\n')

    return lista
   

def expande(nodo):
    listaNodos = []

    for tupla in sucessor(nodo.estado):
        listaNodos.append( Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1))

    return listaNodos



def bfs(fila):
    return fila.popleft() #Deleta o primeiro


def dfs(lista):
    return lista.pop()  #Deleta o ultimo


def caminho(nodo):

    listaCaminho = []

    while nodo.pai is not None:
        listaCaminho.append(nodo.acao)
        nodo = nodo.pai

    listaCaminho.reverse()

    return listaCaminho


def busca_grafo(string, objetivo):
    eXplorados = set()
    Fronteira = deque([Nodo(string, None, None, 0)])

    while (len(Fronteira) != 0):
        v = bfs(Fronteira)

        if (v.estado == objetivo):
            return caminho(v)

        if (v.estado not in eXplorados):
            eXplorados.add(v.estado)
            Fronteira.extend(expande(v))

    return None

def hamming(str, objetivo):

    counter = 0
    for i in range(len(str)):
        if str[i]!=objetivo[i]:
            counter += 1

    return counter     


def manhattan(str, objetivo): 

    str_matriz=stringToMatrix3x3(str)
    objetivo_matriz=stringToMatrix3x3(objetivo)
    counter = 0
    for i in range(len(str_matriz)):
        for j in range(len(str_matriz[i])):
            for k in range(len(objetivo_matriz)):
                for l in range(len(objetivo_matriz[k])):
                    if(str_matriz[i][j]==objetivo_matriz[k][l] and str_matriz[i][j]!='_'):
                        counter+=abs(i-k)+abs(j-l)
                        break
    return counter       

def busca_grafo_heurisitica(string, objetivo):
    
    eXplorados = set()
    Fronteira = []
    heappush(Fronteira, (0, 0, Nodo(string, None, None, 0)))

    counter=0
    while (len(Fronteira) != 0):
        v = heappop(Fronteira)[2]

        if (v.estado == objetivo):
            return caminho(v)

        if (v.estado not in eXplorados):
            eXplorados.add(v.estado)
            for nodo in expande(v):
                counter+=1
                tup = (nodo.custo+manhattan(nodo.estado, objetivo), counter, nodo)
                heappush(Fronteira, tup)
                

    return None


#Pai = Nodo("123456_78", 0, None, 0)
#expande(Pai)

#print(busca_grafo("2_3541687", "12345678_"))

#print(resolve("2_3541687", busca_grafo_heurisitica("2_3541687", "12345678_")))

#print(resolve("2_3541687", busca_grafo("2_3541687", "12345678_")))
