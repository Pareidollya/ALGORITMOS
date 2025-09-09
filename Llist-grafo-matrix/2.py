# GRAFO DA SILVA

# 1. Vértices:
# O número de linhas e colunas da matriz é igual ao número de vértices do grafo.
# 2. Arestas:
# Se matriz[i][j] = 1, significa que existe uma aresta entre o vértice i e o vértice j.
# Se matriz[i][j] = 0, indica que não há uma aresta entre esses dois vértices.
# Em grafos ponderados, o valor matriz[i][j] pode ser o peso da aresta, em vez de apenas 1.

# 3. Tipos de Grafos:
# Não Direcionados: A matriz é simétrica, pois se há uma aresta de i para j, há também de j para i.

# adicionar vertice + i, j = + 0
# adicionar aresta (ligar vertices) adicionar valor X entre vertices
# verificar grau de vertices


# ler grafo (pegar uma matrix como entrada)
# matrix1 [[3, 5, 4, 5], [0, 10, 8, 10]]
import re


class Grafo:
    def __init__(self, matrix: list[list[int]] = []):
        self.matrix = matrix
        # if len(self.matrix) != len(self.matrix[0]):
        #     raise ValueError("Matrix nao simetrica :s")
        # pass
        # m = [[1,0,1],[0,0,0]] -> [[1,0,1],
        #   [0,0,0]]

    # linha = [], coluna = valor dentro da lista, adicionar = +[] +valor dentro das linha

    def addVertice(self, num_v=1, show=True):
        vertices = len(self.matrix)
        new_vl = ([0] * vertices) + ([0] * num_v)
        for i in range(vertices):
            for j in range(num_v):
                self.matrix[i].append(0)
                print("adicionado") if show else ""
        self.matrix.append(new_vl)

    def showMatrix(self):
        top_label = "  "
        for j in range(len(self.matrix)):
            top_label += f" {j} "
        print(top_label)
        for i in range(len(self.matrix)):
            print(f"{i} ", end="")
            print(self.matrix[i])
        print("\n")

    def link(self, v: int, i: int, link=True):
        self.matrix[v][i] = 1 if link else 0
        self.matrix[i][v] = 1 if link else 0

    def linkFromArr(self, v: int, vertices=[]):
        for i in vertices:
            self.link(v, i)

    def getGrau(self, v: int) -> int:
        grau = 0
        for i in self.matrix[v]:
            grau += 1 if i > 0 else 0
        return grau

    def getGraph(self, v_start=0):
        vertice_0 = 0
        for i in range(len(self.matrix)):
            v = ""
            for j in range(len(self.matrix[i])):
                v += f'{j if self.matrix[i][j] > 0 else ""} '
            print(f"{vertice_0} -> ({v})")
            vertice_0 += 1

    def getArestasReg(self):
        a = 0
        vistos = []  # vertices q ja passaram
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] > 0 and j not in vistos:
                    a += 1
            vistos.append(i)
        return a


a = Grafo()
a.addVertice()
a.addVertice()
a.addVertice()
a.linkFromArr(0, [1, 2])
a.link(2, 1)
# a.link(1, 1)
a.showMatrix()
a.getGraph()
print(a.getArestasReg(), "Arestas")
