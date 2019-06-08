import numpy as np

class Digrafo:
    def __init__(self, n_vertices= 0, n_arestas = 0, lista_adj = []):
        self.__n_vertices = n_vertices
        self.__n_arestas = n_arestas
        self.__lista_adj = lista_adj
    
    def __str__(self):
        return f'Vertices: {self.__n_vertices},\nArestas: {self.__n_arestas},\nLista:\n{self.__lista_adj}'

    def __repr__(self):
        return f'Vertices: {self.__n_vertices},\nArestas: {self.__n_arestas},\nLista:\n{self.__lista_adj}'

    def inicializar_lista(self):
        lista_adjacencia = np.array([Node() for i in range(self.__n_vertices)])
        self.__lista_adj = lista_adjacencia
        
    def inserir_aresta(self, v1, v2):
        if(self.__lista_adj[v1].vertice == None):
            self.__lista_adj[v1].vertice = v2
            self.__lista_adj[v1].proximo_vertice = Node()
        else:
            node = self.__lista_adj[v1].proximo_vertice
            while(node != None):
                if(node.proximo_vertice == None):
                    node.vertice = v2
                    node.proximo_vertice = Node()
                    break
                node = node.proximo_vertice

    def mostrar_lista(self):
        for i in range(self.__n_vertices):
            if(self.__lista_adj[i].vertice != None):
                print(f'Vertice: {i}')
                print(f'{self.__lista_adj[i].vertice}->')
                node = self.__lista_adj[i].proximo_vertice
                while(node != None):
                    print(f'{node.vertice}->')
                    node = node.proximo_vertice
            print('\n')
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
    def lista_adj(self):
        return self.__lista_adj
    
    @lista_adj.setter
    def lista_adj(self, valor):
        self.__lista_adj = valor

class Node:
    def __init__(self, vertice = None, proximo_vertice = None):
        self.__vertice = vertice
        self.__proximo_vertice = proximo_vertice
    
    def __str__(self):
        return f'{self.__vertice} {self.__proximo_vertice}'

    def __repr__(self):
        return f'{self.__vertice} {self.__proximo_vertice}'
    
    @property
    def vertice(self):
        return self.__vertice
    
    @vertice.setter
    def vertice(self, valor):
        self.__vertice = valor
    
    @property
    def proximo_vertice(self):
        return self.__proximo_vertice
    
    @proximo_vertice.setter
    def proximo_vertice(self, valor):
        self.__proximo_vertice = valor