import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        self.paraiba = MeuGrafo()
        self.paraiba.adiciona_vertice("J")
        self.paraiba.adiciona_vertice("C")
        self.paraiba.adiciona_vertice("E")
        self.paraiba.adiciona_vertice("P")
        self.paraiba.adiciona_vertice("M")
        self.paraiba.adiciona_vertice("T")
        self.paraiba.adiciona_vertice("Z")
        self.paraiba.adiciona_aresta("a1", "J", "C")
        self.paraiba.adiciona_aresta("a2", "C", "E")
        self.paraiba.adiciona_aresta("a3", "C", "E")
        self.paraiba.adiciona_aresta("a4", "C", "P")
        self.paraiba.adiciona_aresta("a5", "C", "P")
        self.paraiba.adiciona_aresta("a6", "C", "M")
        self.paraiba.adiciona_aresta("a7", "C", "T")
        self.paraiba.adiciona_aresta("a8", "M", "T")
        self.paraiba.adiciona_aresta("a9", "T", "Z")
        self.paraiba.adiciona_aresta("a10", "J", "J")

        self.ComCiclo = MeuGrafo()
        self.ComCiclo.adiciona_vertice("A")
        self.ComCiclo.adiciona_vertice("B")
        self.ComCiclo.adiciona_vertice("C")
        self.ComCiclo.adiciona_vertice("D")
        self.ComCiclo.adiciona_vertice("E")
        self.ComCiclo.adiciona_vertice("F")
        self.ComCiclo.adiciona_vertice("G")
        self.ComCiclo.adiciona_vertice("H")
        self.ComCiclo.adiciona_vertice("I")
        self.ComCiclo.adiciona_vertice("J")
        self.ComCiclo.adiciona_aresta("e1", "A", "B")
        self.ComCiclo.adiciona_aresta("e2", "A", "C")
        self.ComCiclo.adiciona_aresta("e3", "B", "C")
        self.ComCiclo.adiciona_aresta("e4", "B", "D")
        self.ComCiclo.adiciona_aresta("e5", "C", "E")
        self.ComCiclo.adiciona_aresta("e6", "D", "E")
        self.ComCiclo.adiciona_aresta("e7", "D", "F")
        self.ComCiclo.adiciona_aresta("e8", "E", "G")
        self.ComCiclo.adiciona_aresta("e9", "F", "G")
        self.ComCiclo.adiciona_aresta("e10", "F", "H")
        self.ComCiclo.adiciona_aresta("e11", "G", "I")
        self.ComCiclo.adiciona_aresta("e12", "H", "I")
        self.ComCiclo.adiciona_aresta("e13", "H", "J")

        self.SemCiclo = MeuGrafo()
        self.SemCiclo.adiciona_vertice("A")
        self.SemCiclo.adiciona_vertice("B")
        self.SemCiclo.adiciona_vertice("C")
        self.SemCiclo.adiciona_vertice("D")
        self.SemCiclo.adiciona_aresta("e1", "A", "B")
        self.SemCiclo.adiciona_aresta("e2", "B", "C")
        self.SemCiclo.adiciona_aresta("e3", "C", "D")

        self.grafo_conexo = MeuGrafo()
        self.grafo_conexo.adiciona_vertice("A")
        self.grafo_conexo.adiciona_vertice("B")
        self.grafo_conexo.adiciona_vertice("C")
        self.grafo_conexo.adiciona_vertice("D")
        self.grafo_conexo.adiciona_vertice("E")
        self.grafo_conexo.adiciona_aresta("a1", "A", "B")
        self.grafo_conexo.adiciona_aresta("a2", "B", "C")
        self.grafo_conexo.adiciona_aresta("a3", "C", "D")
        self.grafo_conexo.adiciona_aresta("a4", "D", "E")
        self.grafo_conexo.adiciona_aresta("a5", "E", "A")

        self.grafo_desconexo = MeuGrafo()
        self.grafo_desconexo.adiciona_vertice("A")
        self.grafo_desconexo.adiciona_vertice("B")
        self.grafo_desconexo.adiciona_vertice("C")
        self.grafo_desconexo.adiciona_vertice("D")
        self.grafo_desconexo.adiciona_vertice("E")
        self.grafo_desconexo.adiciona_aresta("a1", "A", "B")
        self.grafo_desconexo.adiciona_aresta("a2", "C", "D")



    def test_Ciclo(self):
        self.assertFalse(self.SemCiclo.ha_ciclo())
        self.assertListEqual(self.ComCiclo.ha_ciclo(), ['A', 'e1', 'B', 'e3', 'C', 'e2', 'A'])
        self.assertListEqual(self.paraiba.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C'])

    def test_conexo(self):
        self.assertTrue(self.grafo_conexo.conexo())
        self.assertFalse(self.grafo_desconexo.conexo())
        self.assertTrue(self.paraiba.conexo())

    def test_caminho(self):
        self.assertListEqual(self.paraiba.caminho(4), ['E', 'a2', 'C', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertFalse(self.paraiba.caminho(8))
        self.assertListEqual(self.ComCiclo.caminho(8),
                             ['A', 'e1', 'B', 'e3', 'C', 'e5', 'E', 'e6', 'D', 'e7', 'F', 'e10', 'H', 'e12', 'I',
                              'e11', 'G'])
        self.assertListEqual(self.grafo_conexo.caminho(3), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'D'])
