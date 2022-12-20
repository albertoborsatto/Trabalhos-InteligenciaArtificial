from utils import *
from collections import deque
from heapq import *
import time

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    lista = []

    matriz = stringToMatrix3x3(estado)

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
        tupla = ("abaixo", swap(estado, 3*i+j, 3*(i+1)+j))
        lista.append(tupla)

    if (i > 0):
        tupla = ("acima", swap(estado, 3*i+j, 3*(i-1)+j))
        lista.append(tupla)

    if (j < 2):
        tupla = ("direita", swap(estado, 3*i+j, 3*i + j+1))
        lista.append(tupla)

    if (j > 0):
        tupla = ("esquerda", swap(estado, 3*i+j, 3*i + j-1))
        lista.append(tupla)

    return lista


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    listaNodos = []

    for tupla in sucessor(nodo.estado):
        listaNodos.append( Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1))

    return listaNodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    eXplorados = set()
    Fronteira = deque([Nodo(estado, None, None, 0)])
    #count = 0
    
    #inicio = time.time()
    while (len(Fronteira) != 0):
        v = Fronteira.popleft()
        
        if (v.estado == "12345678_"):
            #final = time.time()
            #print(f'Expandidos bfs => {count}')
            #print(f'Tempo bfs => {final-inicio}')
            return caminho(v)

        if (v.estado not in eXplorados):
            #count += 1
            eXplorados.add(v.estado)
            Fronteira.extend(expande(v))

    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    eXplorados = set()
    Fronteira = deque([Nodo(estado, None, None, 0)])
    #count = 0
    
    #inicio = time.time()
    while (len(Fronteira) != 0):
        v = Fronteira.pop()

        if (v.estado == "12345678_"):
            #final = time.time()
            #print(f'Expandidos dfs => {count}')
            #print(f'Tempo dfs => {final-inicio}')
            return caminho(v)

        if (v.estado not in eXplorados):
            #count += 1
            eXplorados.add(v.estado)
            Fronteira.extend(expande(v))

    return None


def hamming(str, objetivo):

    counter = 0
    for i in range(len(str)):
        if str[i]!=objetivo[i]:
            counter += 1

    return counter  

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    eXplorados = set()
    Fronteira = []
    heappush(Fronteira, (0, 0, Nodo(estado, None, None, 0)))
    #count = 0
    counter=0

    #inicio = time.time()
    while (len(Fronteira) != 0):
        v = heappop(Fronteira)[2]

        if (v.estado == "12345678_"):
            #final = time.time()
            #print(f'Expandidos hamming => {count}')
            #print(f'Tempo hamming => {final-inicio}')
            return caminho(v)

        if (v.estado not in eXplorados):
            #count += 1
            eXplorados.add(v.estado)
            for nodo in expande(v):
                counter+=1
                tup = (nodo.custo + hamming(nodo.estado, "12345678_"), counter, nodo)
                heappush(Fronteira, tup)
                

    return None


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


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    eXplorados = set()
    Fronteira = []
    heappush(Fronteira, (0, 0, Nodo(estado, None, None, 0)))
    counter=0
    #count = 0
   
    #inicio = time.time()
    while (len(Fronteira) != 0):
        v = heappop(Fronteira)[2]

        if (v.estado == "12345678_"):
            #final = time.time()
            #print(f'Expandidos manhattan => {count}')
            #print(f'Tempo manhattan => {final - inicio}')
            return caminho(v)

        if (v.estado not in eXplorados):
            #count += 1
            eXplorados.add(v.estado)
            for nodo in expande(v):
                counter+=1
                tup = (nodo.custo + manhattan(nodo.estado, "12345678_"), counter, nodo)
                heappush(Fronteira, tup)
                
    return None


#bfs("2_3541687")
#dfs("2_3541687")
#astar_hamming("2_3541687")
#astar_manhattan("2_3541687")