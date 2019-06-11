from math import radians, cos, sin, asin, sqrt
import sys
import numpy as npf

def distancia(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def minDistance(n_vertices, dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxsize

    # Search not nearest vertex not in the 
    # shortest path tree
    for v in range(n_vertices):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(matriz_adj, n_vertices, v1):
 
    dist = [sys.maxsize] * n_vertices
    dist[v1] = 0
    sptSet = [False] * n_vertices

    for cout in range(n_vertices):
        # Pick the minimum distance vertex from 
        # the set of vertices not yet processed. 
        # u is always equal to v1 in first iteration
        u = minDistance(n_vertices ,dist, sptSet)

        # Put the minimum distance vertex in the 
        # shotest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices 
        # of the picked vertex only if the current 
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(n_vertices):
            if matriz_adj[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + matriz_adj[u][v]:
                    dist[v] = dist[u] + matriz_adj[u][v]

    return dist

def custo(dados):
    custos = npf.full((len(dados),len(dados)), 0)
    for i in range(len(dados)):
        for j in range(len(dados)):
            if(i != j and j!= 0):
                custos[i,j] = distancia(float(dados[0]['longitude']), float(dados[0]['latitude']), float(dados[j]['longitude']), float(dados[j]['latitude']))
    return custos