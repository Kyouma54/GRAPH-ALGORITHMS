import numpy as np

class Digrafo:
    def __init__(self, n_vertices= 0, n_arestas = 0, matriz_adj = []):
        self.__n_vertices = n_vertices
        self.__n_arestas = n_arestas
        self.__matriz_adj = matriz_adj
    
    def __str__(self):
        return f'Vertices: {self.__n_vertices},\nArestas: {self.__n_arestas},\nMatriz:\n{self.__matriz_adj}'

    def __repr__(self):
        return f'Vertices: {self.__n_vertices},\nArestas: {self.__n_arestas},\nMatriz:\n{self.__matriz_adj}'

    def inicializar_matriz(self, valor):
        matriz_adjacencia = np.full((self.__n_vertices, self.__n_vertices), valor)
        self.__matriz_adj = matriz_adjacencia
        
    def inserirAresta(self, v1, v2):
        if(v1 != v2 and self.__matriz_adj[v1-1,v2-1] == 0):
            self.__matriz_adj[v1-1,v2-1] = 1
            self.n_arestas += 1
    
    def mostrarMatriz(self):
        print(self.__matriz_adj)

    @property
    def n_vertices(self):
        return self.__n_vertices
    
    @n_vertices.setter
    def n_vertices(self, valor):
        self.__n_vertices = valor

    @property
    def n_arestas(self):
        return self.__n_arestas
    
    @n_arestas.setter
    def n_arestas(self, valor):
        self.__n_arestas = valor
    
    @property
    def matriz_adj(self):
        return self.__matriz_adj
    
    @matriz_adj.setter
    def matriz_adj(self, valor):
        self.__matriz_adj = valor