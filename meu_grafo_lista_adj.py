from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *



class MeuGrafo(GrafoListaAdjacencia):
    def adjacentes(self, V1,V2):
        #adicionei essa função pois achei necessaria
        for a in self.arestas.values():
            if (a.v1 == V1 and a.v2 == V2) or (a.v1 == V2 and a.v2== V1):
                return True
        return False
                

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        vertices = self.vertices
        nao_adjacentes = set()
        
        for v1 in vertices:
            for v2 in vertices:
                if v1!=v2 and not self.adjacentes(v1,v2):
                    nao_adjacentes.add(f"{v1}-{v2}")
        
        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas.values():
            if a.v1 == a.v2:
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
        
        grau = 0
        
        for a in self.arestas.values():
            if V == a.v1.rotulo:
                grau +=1
            if V == a.v2.rotulo:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.arestas.values():
            for A in self.arestas.values():
                if a.v1 == A.v1 and a.v2 == A.v2:
                    return True
                if a.v1 == A.v2 and a.v2 == A.v1:
                    return True
        return False
                

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista = list()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"O grafo não possui vertice com esse rótulo.")
        
        for a in self.arestas.values():
            if a.v1.rotulo == V:
                lista.append(a.rotulo)
            elif a.v2.rotulo == V:
                lista.append(a.rotulo)
        return lista
            
             

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        return not bool(self.vertices_nao_adjacentes())
    
    # Roteiro 2
    def dfs_aux(self, grafo_retorno, vertice):
        arestas_incidentes = self.arestas_sobre_vertice(vertice)

        if (not grafo_retorno.existe_rotulo_vertice(vertice)):
            grafo_retorno.adiciona_vertice(vertice)

        for a in arestas_incidentes:
            if (a.rotulo not in grafo_retorno.arestas):
                if (vertice != a.v1.rotulo):
                    no_destino = a.v1.rotulo
                else:
                    no_destino = a.v2.rotulo

                if (not grafo_retorno.existe_rotulo_vertice(no_destino)):
                    grafo_retorno.adiciona_vertice(no_destino)
                    grafo_retorno.adiciona_aresta(a.rotulo, vertice, no_destino)
                    self.dfs_aux(grafo_retorno, no_destino)

        return grafo_retorno

    def dfs(self, V=''):
        grafo_retorno = MeuGrafo()
        return self.dfs_aux(grafo_retorno, V)
    
    
    def bfs(self, V=''):
        arvore_bfs = MeuGrafo()

        def bfs_r(V):
            if not arvore_bfs.existe_rotulo_vertice(V):
                arvore_bfs.adiciona_vertice(V)
            vertices_visitados = []

            for aresta in self.arestas_sobre_vertice(V):
                if self.get_aresta(aresta).v1.rotulo == V:
                    v = self.get_aresta(aresta).v2.rotulo
                else:
                    v = self.get_aresta(aresta).v1.rotulo

                if not arvore_bfs.existe_rotulo_vertice(v):
                    arvore_bfs.adiciona_vertice(v)
                    vertices_visitados.append(v)
                    arvore_bfs.adiciona_aresta(aresta, V, v)

            for v in vertices_visitados:
                bfs_r(v)

        bfs_r(V)
        return arvore_bfs
    
    
    # Roteiro 3
    def caminho(self, n):
        achou = False
        ver = self.vertices
        vertices = []
        caminho = []
        for v in ver:
            vertices.append(v.rotulo)

        vertices.sort()

        def caminho_r(v, c, n, achou):
            if n == 0 or achou:
                achou = True
                return (c, achou)

            arestas = self.arestas_sobre_vertice(v)
            arr = []
            for a in arestas:
                arr.append(a)

            arr.sort()

            if len(c) == 0:
                c.append(v)

            for aresta in arr:
                v2 = v
                if self.arestas[aresta].v1.rotulo == v and self.arestas[aresta].v2.rotulo != c[-1]:
                    v2 = self.arestas[aresta].v2.rotulo
                elif self.arestas[aresta].v2.rotulo == v and self.arestas[aresta].v1.rotulo != c[-1]:
                    v2 = self.arestas[aresta].v1.rotulo

                if v2 not in c:
                    c.append(aresta)
                    c.append(v2)
                    c, achou = caminho_r(v2, c, n - 1, achou)

                if achou:
                    return (c, achou)
            try:
                c.pop()
                c.pop()
            except:
                pass

            return (c, achou)

        for vertice in vertices:
            caminho, achou = caminho_r(vertice, caminho, n, achou)
            if achou:
                break

        if caminho == []:
            return False
        return caminho

    def conexo(self):
        vertices = self.vertices

        aux = MeuGrafo()
        aux = self.bfs(vertices[0].rotulo)

        for vertice in vertices:
            if not aux.existe_rotulo_vertice(vertice.rotulo):
                return False

        return True

    def ha_ciclo(self):
        achou = False
        ver = self.vertices
        vertices = []
        caminho = []
        for v in ver:
            vertices.append(v.rotulo)

        vertices.sort()

        def ciclo_r(v, c, achou):
            if achou:
                achou = True
                return (c, achou)

            arestas = self.arestas_sobre_vertice(v)
            arr = []
            for a in arestas:
                arr.append(a)

            arr.sort()

            if len(c) == 0:
                c.append(v)

            for aresta in arr:
                if self.arestas[aresta].v1.rotulo == v:
                    v2 = self.arestas[aresta].v2.rotulo
                elif self.arestas[aresta].v2.rotulo == v:
                    v2 = self.arestas[aresta].v1.rotulo

                if (len(c) != 0 and c[0] == v2) and aresta not in c:
                    c.append(aresta)
                    c.append(v2)
                    achou = True
                    return (c, achou)

                if v2 not in c:
                    c.append(aresta)
                    c.append(v2)
                    c, achou = ciclo_r(v2, c, achou)

                if achou:
                    return (c, achou)
            try:
                c.pop()
                c.pop()
            except:
                pass

            return (c, achou)

        for vertice in vertices:
            caminho, achou = ciclo_r(vertice, caminho, achou)
            if achou:
                break

        if caminho == []:
            return False
        return caminho
    



