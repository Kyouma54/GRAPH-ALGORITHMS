from Vertice import Vertice

#Um Arco Pode ser considerada como uma Aresta
class Aresta:
    def __init__(self, v1, v2):
        self.v1 = Vertice(v1)
        self.v2 = Vertice(v2)

    def criar_arco(self, v1, v2):
        novo_arco = Aresta(v1,v2)
        return novo_arco
