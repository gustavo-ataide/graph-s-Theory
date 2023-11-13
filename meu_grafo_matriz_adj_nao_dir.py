import copy
from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
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


        lista= set()
        for v1 in self.vertices:
            for v2 in self.vertices:
                if v1.rotulo != v2.rotulo:
                    if v1.rotulo not in vertices_adjacentes(v2.rotulo):
                        if f"{v1.rotulo}-{v2.rotulo}" not in lista and f"{v2.rotulo}-{v1.rotulo}" not in lista:
                            lista.add(f"{v1.rotulo}-{v2.rotulo}")
        return lista



    def ha_laco(self):
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
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"O grafo não possui vertice com esse rotulo")
        vertice = self.get_vertice(V)
        cont=0
        for dic_a in self.arestas:
            for list_a in dic_a:
                if len(list_a) != 0:
                    for a in list_a:
                        if self.get_aresta(a).v1 == vertice and self.get_aresta(a).v2 == vertice:
                            cont+=4
                        elif self.get_aresta(a).v1 == vertice:
                            cont+=1
                        elif self.get_aresta(a).v2 == vertice:
                            cont+=1



        return cont/2

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                dicionario_arestas = self.arestas[i][j]
                contiguais=0
                if len(dicionario_arestas)>1:
                    for aresta in dicionario_arestas:
                        for aresta2 in dicionario_arestas:

                            if dicionario_arestas[aresta] == dicionario_arestas[aresta2]:
                                contiguais+=1
                if contiguais>=2:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
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
        vertices = self.vertices
        qtd_ver = len(vertices)
        auxiliar = []
        for l in range(qtd_ver):
            linha = []
            for c in range(qtd_ver):
                if len(self.arestas[l][c]) > 0:
                    linha.append(1)
                else:
                    linha.append(0)
            auxiliar.append(linha)

        for i in range(qtd_ver):
            for j in range(qtd_ver):
                if auxiliar[j][i] == 1:
                    for k in range(qtd_ver):
                        if auxiliar[j][k] == 1 or auxiliar[i][k] == 1:
                            auxiliar[j][k] = 1
        return auxiliar



g_p = MeuGrafo()
g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'C', 'E')
g_p.adiciona_aresta('a4', 'P', 'C')
g_p.adiciona_aresta('a5', 'P', 'C')
g_p.adiciona_aresta('a6', 'T', 'C')
g_p.adiciona_aresta('a7', 'M', 'C')
g_p.adiciona_aresta('a8', 'M', 'T')
g_p.adiciona_aresta('a9', 'T', 'Z')
# g_p.adiciona_aresta('a10', 'T', 'T')

print(g_p)


grafinho = MeuGrafo()
grafinho.adiciona_vertice("J")
grafinho.adiciona_vertice("C")
grafinho.adiciona_aresta("a1","J","C")
