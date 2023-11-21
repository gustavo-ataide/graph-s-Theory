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




    def dijkstra(self, inicio, fim):
        if self.ha_laco() or self.ha_paralelas():
            return False
        
        for vertice in self.vertices:
            vertice.Beta = float('inf')
            vertice.Total_Visitado = False
            vertice.Predecessor = 0
            vertice.W = self.get_vertice(inicio)

        self.get_vertice(inicio).Beta = 0
        self.get_vertice(inicio).Total_Visitado = True
        menorbeta = float('inf')
        def acha_r(self,menorbeta):

            r = None
            for v in self.vertices:
                if v.Total_Visitado == False and v.Beta < float('inf') and v.Beta < menorbeta:
                    menorbeta = v.Beta
                    v.Total_Visitado = True
                    self.W = v
                    r = self
                    return r, menorbeta

            return r, menorbeta

        for vertice in self.vertices:
            if vertice.Total_Visitado == False:


                for aresta in self.arestas_sobre_vertice(vertice.rotulo):
                    aresta = self.get_aresta(aresta)
                    if vertice.Beta > vertice.W.Beta + aresta.peso:
                        vertice.Beta = vertice.W.Beta + aresta.peso
                        vertice.Predecessor = vertice.W

                r,menorbeta = acha_r(self,menorbeta)
                if r is None:
                    self.get_vertice(fim).Predecessor = self.W
                    break
                while self.W != self.get_vertice(fim):
                    r,menorbeta = acha_r(self,menorbeta)
                    if r is None:
                        break
                    self = r


        def predec(self,inicio,lista,vertice):
            lista.append(vertice.rotulo)
            if vertice == inicio:
                return lista
            return predec(self,inicio,lista,vertice.Predecessor)

        lista_vertices = []
        lista_vertices = predec(self,self.get_vertice(inicio),lista_vertices,self.get_vertice(fim))

        return lista_vertices[::-1]



    def bellman_ford(self,inicio,fim):
        for vertice in self.vertices:
            vertice.Pi = None
            vertice.Pai = float('inf')
        self.get_vertice(inicio).Pai = 0
        
        for i in range(len(self.vertices)-1):
            for aresta in self.arestas_sobre_vertice(self.vertices[i].rotulo):
                aresta = self.get_aresta(aresta)
                
                if aresta.v1 == self.vertices[i]:
                    if aresta.peso + self.get_vertice(aresta.v1.rotulo).Pai < self.get_vertice(aresta.v2.rotulo).Pai:
                        self.get_vertice(aresta.v2.rotulo).Pai = aresta.peso + self.get_vertice(aresta.v1.rotulo).Pai
                        self.get_vertice(aresta.v2.rotulo).Pi = self.get_vertice(aresta.v1.rotulo)

                if aresta.v2 == self.vertices[i]:
                    if aresta.peso + self.get_vertice(aresta.v2.rotulo).Pai < self.get_vertice(aresta.v1.rotulo).Pai:
                        self.get_vertice(aresta.v1.rotulo).Pai = aresta.peso + self.get_vertice(aresta.v2.rotulo).Pai
                        self.get_vertice(aresta.v1.rotulo).Pi = self.get_vertice(aresta.v2.rotulo)

        
        #se depois disso continuar relaxando, retorno falso
        for i in range(len(self.vertices)-1):
            for aresta in self.arestas_sobre_vertice(self.vertices[i].rotulo):
                aresta = self.get_aresta(aresta)
                if aresta.v1 == self.vertices[i]:
                    if aresta.peso + self.get_vertice(aresta.v1.rotulo).Pai < self.get_vertice(aresta.v2.rotulo).Pai:
                        return False

                if aresta.v2 == self.vertices[i]:
                    if aresta.peso + self.get_vertice(aresta.v2.rotulo).Pai < self.get_vertice(aresta.v1.rotulo).Pai:
                        return False

        #agora basta achar o caminho
        def predec(self,inicio,lista,vertice):
            lista.append(vertice.rotulo)
            if vertice == inicio:
                return lista
            return predec(self,inicio,lista,vertice.Pi)

        lista_vertices = []
        lista_vertices = predec(self,self.get_vertice(inicio),lista_vertices,self.get_vertice(fim))
        return lista_vertices[::-1]



g_dijkstra = MeuGrafo()
g_dijkstra.adiciona_vertice("A")
g_dijkstra.adiciona_vertice("B")
g_dijkstra.adiciona_vertice("C")
g_dijkstra.adiciona_vertice("D")
g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
g_dijkstra.adiciona_aresta('3', 'B', 'D', 7)
g_dijkstra.adiciona_aresta('2', 'C', 'D', 1)

print(g_dijkstra.dijkstra("A","D"))
