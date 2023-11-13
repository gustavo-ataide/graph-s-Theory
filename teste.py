from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_lista_adj import *
from meu_grafo_lista_adj import MeuGrafo
import unittest


#Roteiro3
class Teste_R3(unittest.TestCase):
    paraiba = MeuGrafo()
    paraiba.adiciona_vertice("J")
    paraiba.adiciona_vertice("C")
    paraiba.adiciona_vertice("E")
    paraiba.adiciona_vertice("P")
    paraiba.adiciona_vertice("M")
    paraiba.adiciona_vertice("T")
    paraiba.adiciona_vertice("Z")
    paraiba.adiciona_aresta("a1", "J", "C")
    paraiba.adiciona_aresta("a2", "C", "E")
    paraiba.adiciona_aresta("a3", "C", "E")
    paraiba.adiciona_aresta("a4", "C", "P")
    paraiba.adiciona_aresta("a5", "C", "P")
    paraiba.adiciona_aresta("a6", "C", "M")
    paraiba.adiciona_aresta("a7", "C", "T")
    paraiba.adiciona_aresta("a8", "M", "T")
    paraiba.adiciona_aresta("a9", "T", "Z")
    paraiba.adiciona_aresta("a10", "J", "J")

    ComCiclo = MeuGrafo()
    ComCiclo.adiciona_vertice("A")
    ComCiclo.adiciona_vertice("B")
    ComCiclo.adiciona_vertice("C")
    ComCiclo.adiciona_vertice("D")
    ComCiclo.adiciona_vertice("E")
    ComCiclo.adiciona_vertice("F")
    ComCiclo.adiciona_vertice("G")
    ComCiclo.adiciona_vertice("H")
    ComCiclo.adiciona_vertice("I")
    ComCiclo.adiciona_vertice("J")
    ComCiclo.adiciona_aresta("e1", "A", "B")
    ComCiclo.adiciona_aresta("e2", "A", "C")
    ComCiclo.adiciona_aresta("e3", "B", "C")
    ComCiclo.adiciona_aresta("e4", "B", "D")
    ComCiclo.adiciona_aresta("e5", "C", "E")
    ComCiclo.adiciona_aresta("e6", "D", "E")
    ComCiclo.adiciona_aresta("e7", "D", "F")
    ComCiclo.adiciona_aresta("e8", "E", "G")
    ComCiclo.adiciona_aresta("e9", "F", "G")
    ComCiclo.adiciona_aresta("e10", "F", "H")
    ComCiclo.adiciona_aresta("e11", "G", "I")
    ComCiclo.adiciona_aresta("e12", "H", "I")
    ComCiclo.adiciona_aresta("e13", "H", "J")

    SemCiclo = MeuGrafo()
    SemCiclo.adiciona_vertice("A")
    SemCiclo.adiciona_vertice("B")
    SemCiclo.adiciona_vertice("C")
    SemCiclo.adiciona_vertice("D")
    SemCiclo.adiciona_aresta("e1", "A", "B")
    SemCiclo.adiciona_aresta("e2", "B", "C")
    SemCiclo.adiciona_aresta("e3", "C", "D")

    grafo_conexo = MeuGrafo()
    grafo_conexo.adiciona_vertice("A")
    grafo_conexo.adiciona_vertice("B")
    grafo_conexo.adiciona_vertice("C")
    grafo_conexo.adiciona_vertice("D")
    grafo_conexo.adiciona_vertice("E")
    grafo_conexo.adiciona_aresta("a1", "A", "B")
    grafo_conexo.adiciona_aresta("a2", "B", "C")
    grafo_conexo.adiciona_aresta("a3", "C", "D")
    grafo_conexo.adiciona_aresta("a4", "D", "E")
    grafo_conexo.adiciona_aresta("a5", "E", "A")

    grafo_desconexo = MeuGrafo()
    grafo_desconexo.adiciona_vertice("A")
    grafo_desconexo.adiciona_vertice("B")
    grafo_desconexo.adiciona_vertice("C")
    grafo_desconexo.adiciona_vertice("D")
    grafo_desconexo.adiciona_vertice("E")
    grafo_desconexo.adiciona_aresta("a1", "A", "B")
    grafo_desconexo.adiciona_aresta("a2", "C", "D")


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
        self.assertListEqual(self.ComCiclo.caminho(8),['A', 'e1', 'B', 'e3', 'C', 'e5', 'E', 'e6', 'D', 'e7', 'F', 'e10', 'H', 'e12', 'I', 'e11', 'G'])
        self.assertListEqual(self.grafo_conexo.caminho(3),['A', 'a1', 'B', 'a2', 'C', 'a3', 'D'])