import copy

from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        def vertices_adjacentes(V=''):
            lista = list()
            arestas = self.arestas_sobre_vertice(V)
            for aresta in arestas:
                a = self.get_aresta(aresta)
                if a.v1.rotulo != a.v2.rotulo:
                    if V == a.v1.rotulo:
                        lista.append(a.v2.rotulo)
                    elif V == a.v2.rotulo:
                        lista.append(a.v1.rotulo)
            return lista
        lista = set()
        for v1 in self.vertices:
            for v2 in self.vertices:
                if v1.rotulo != v2.rotulo:
                    if v1.rotulo not in vertices_adjacentes(v2.rotulo):
                        if f"{v1.rotulo}-{v2.rotulo}" not in lista and f"{v2.rotulo}-{v1.rotulo}" not in lista:
                            lista.add(f"{v1.rotulo}-{v2.rotulo}")
        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for dic_a in self.arestas:
            for list_a in dic_a:
                if len(list_a) != 0:
                    for a in list_a:
                        if self.get_aresta(a).v1 == self.get_aresta(a).v2:
                            return True

        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"O grafo não possui vertice com esse rotulo")
        vertice = self.get_vertice(V)
        cont = 0
        for dic_a in self.arestas:
            for list_a in dic_a:
                if len(list_a) != 0:
                    for a in list_a:
                        if self.get_aresta(a).v1 == vertice and self.get_aresta(a).v2 == vertice:
                            cont += 4
                        elif self.get_aresta(a).v1 == vertice:
                            cont += 1
                        elif self.get_aresta(a).v2 == vertice:
                            cont += 1

        return cont / 2

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                dicionario_arestas = self.arestas[i][j]
                contiguais = 0
                if len(dicionario_arestas) > 1:
                    for aresta in dicionario_arestas:
                        for aresta2 in dicionario_arestas:

                            if dicionario_arestas[aresta] == dicionario_arestas[aresta2]:
                                contiguais += 1
                if contiguais >= 2:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"O grafo não possui vertice com esse rotulo")

        lista = list()
        for list_a in self.arestas:
            for dic_a in list_a:
                if len(list_a) != 0:
                    for a in dic_a:
                        if self.get_aresta(a).v1.rotulo == V and a not in lista:
                            lista.append(a)
                        elif self.get_aresta(a).v2.rotulo == V and a not in lista:
                            lista.append(a)

        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        return not bool(self.vertices_nao_adjacentes())

    def warshall(self):
        E = copy.deepcopy(self)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self[j][i] == 0:
                    for k in range(len(self.vertices)):
                        if E[j][k] < E[i][k]:
                            E[j][k] = E[i][k]
        return E


    #legenda: inicio == u / fim == v
                #pesoaresta(r-s) == alfa(r-s)
                #peso do menor caminho entre u-r == B(r)
                #visitadoSN == bool FI
                #predecessor == PI=0

    #peso tem que ser positivo


    # def dijkstra(self, inicio, fim):
    #     if self.ha_laco():
    #         return False
    #
    #     # if self.ha_paralelas():
    #     #     return False
    #
    #     for vertice in self.vertices:
    #         vertice.Beta = float('inf')
    #         vertice.Total_Visitado = False
    #         vertice.Predecessor = 0
    #         vertice.W = self.get_vertice(inicio)
    #
    #     self.get_vertice(inicio).Beta = 0
    #     self.get_vertice(inicio).Total_Visitado = True
    #
    #     for vertice in self.vertices:
    #         if vertice.Total_Visitado == False:
    #             print(vertice.Beta)
    #
    #             for aresta in self.arestas_sobre_vertice(vertice.rotulo):
    #                 aresta = self.get_aresta(aresta)
    #                 if vertice.Beta > vertice.W.Beta + aresta.peso:
    #                     vertice.Beta = vertice.W.Beta + aresta.peso
    #                     vertice.Predecessor = vertice.W
    #
    #             if vertice.Total_Visitado==False and vertice.Beta < float('inf') and
    def dijkstra(self, inicio, fim):
        self.W = self.get_vertice(inicio)
        if self.ha_laco():
            return False

        for vertice in self.vertices:
            vertice.Beta = float('inf')
            vertice.Total_Visitado = False
            vertice.Predecessor = 0

        self.get_vertice(inicio).Beta = 0
        self.get_vertice(inicio).Total_Visitado = True


        while True:
            min_beta = float('inf')
            min_vertice = None



                    #if self.W == fim:
            print(self.W)





            for aresta in self.arestas_sobre_vertice(min_vertice.rotulo):
                aresta = self.get_aresta(aresta)
                if min_vertice.Beta > self.W.Beta + aresta.peso:
                    min_vertice.Beta = self.W.Beta + aresta.peso
                    min_vertice.Predecessor = self.W

                    min_vertice.Total_Visitado = True
                    self.W = min_vertice



            for vertice in self.vertices:
                if vertice.Total_Visitado == False and vertice.Beta < min_beta:
                    min_beta = vertice.Beta
                    min_vertice = vertice

            if min_vertice is None:
                break

            self.get_vertice(min_vertice).Total_Visitado = True
            min_vertice.Total_Visitado = True





    # def dijkstra_aux(self, inicio,fim):







g_dijkstra = MeuGrafo()
g_dijkstra.adiciona_vertice("A")
g_dijkstra.adiciona_vertice("B")
g_dijkstra.adiciona_vertice("C")
g_dijkstra.adiciona_vertice("D")
g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
g_dijkstra.adiciona_aresta('3', 'B', 'D', 1)
g_dijkstra.adiciona_aresta('2', 'C', 'D', 2)
g_dijkstra.dijkstra("A","D")
