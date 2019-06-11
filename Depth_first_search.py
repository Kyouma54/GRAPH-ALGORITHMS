import numpy as np

vertice_visitado = np.zeros(1000, dtype=int)

def buscar(digrafo, v1, v2):
    percorrerVertices(digrafo, v1, 0)

    if(vertice_visitado[v2] != 0):
        return True
    else:
        return False

def percorrerVertices(digrafo, v1, contador):
    vertice_visitado[v1] = contador + 1 
    
    for i in range(digrafo.n_vertices):
        if(digrafo.matriz_adj[v1][i] != 0 and vertice_visitado[i] == 0):
            percorrerVertices(digrafo, i, vertice_visitado[v1])
    