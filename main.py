from Digrafo import Digrafo
import Depth_first_search as dfs
import Finder
import csv as maincsv
import json as mainjson

def main():
    #Abrindo csv e gerando json
    csv = open('./dados/dados.csv', 'r')
    json = open('./dados/dados.json', 'w')
    column = ("nome", "latitude", "longitude", "estado")

    dados_csv = maincsv.DictReader(csv, column)
    dados_json = mainjson.dumps([x for x in dados_csv])
    json.write(dados_json)

    dados_json = mainjson.loads(dados_json)

    csv.close()
    json.close()

    #Testando Dijsktra com Digrafo Normal
    print('Teste Dijkstra')
    d1 = Digrafo(6)
    d1.inicializar_matriz(0)
    d1.inserir_aresta(0, 2, 7)
    d1.inserir_aresta(0, 4, 4)
    d1.inserir_aresta(0, 3, 2)
    d1.inserir_aresta(1, 2, 0)
    d1.inserir_aresta(2, 4, 1)
    d1.inserir_aresta(3, 4, 1)
    d1.inserir_aresta(3, 5, 3)
    d1.inserir_aresta(4, 1, 4)
    d1.inserir_aresta(4, 5, 1)
    d1.inserir_aresta(5, 1, 2)
    d1.mostrar_matriz()
    distancia = Finder.dijkstra(d1.matriz_adj, d1.n_vertices, 0)
    print(distancia)

    #Calculando distancias entre coordenadas
    print('\nTeste Distancia entre Coordenadas')
    print(Finder.distancia(float(dados_json[0]['longitude']), float(dados_json[0]['latitude']), float(dados_json[1]['longitude']), float(dados_json[1]['latitude'])))

    #Calculando custos e gerando array
    print('\nTeste Matriz com custos')
    print(Finder.custo(dados_json))

    #Inicio do trabalho implementacional
    print('\nTeste dijsktra + Coordenadas')
    entrada = int(input('Raio: '))
    d2 = Digrafo(len(dados_json))
    d2.inicializar_matriz(0)
    d2.matriz_adj = d2.matriz_adj + Finder.custo(dados_json)
    d2.mostrar_matriz()
    distancia2 = Finder.dijkstra(d2.matriz_adj, d2.n_vertices, 0)
    print(distancia2)


if __name__ == '__main__':
    main()
