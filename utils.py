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
    

def caminho(nodo, busca):

    listaCaminho = []
    count = 0
    
    while nodo.pai is not None:
        listaCaminho.append(nodo.acao)
        nodo = nodo.pai
        if(busca == 'hamming'):
            count += nodo.custo + hamming(nodo.estado, "12345678_")
        elif(busca == 'manhattan'):
            count += nodo.custo + manhattan(nodo.estado, "12345678_")
        else:
            count += nodo.custo
        
    listaCaminho.reverse()
    #print(f'Custo soluÃ§Ã£o => {count}\n\n')

    return listaCaminho