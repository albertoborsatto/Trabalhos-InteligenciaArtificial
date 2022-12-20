def stringToMatrix3x3(string):
    matriz = []
    aux = []

    for i in range(int(len(string)/3)):
        aux.append(string[3*i])
        aux.append(string[3*i+1])
        aux.append(string[3*i+2])

        matriz.append(aux.copy())
        aux.clear()

    return matriz


def swap(entrada, i, j):
    entrada = list(entrada)
    entrada[i], entrada[j] = entrada[j], entrada[i]
    return "".join(entrada)
    

def caminho(nodo):

    listaCaminho = []
    #count = 0
    
    while nodo.pai is not None:
        listaCaminho.append(nodo.acao)
        nodo = nodo.pai
        #count += nodo.custo
        
    listaCaminho.reverse()
    #print(f'Custo solução => {count}\n\n')

    return listaCaminho