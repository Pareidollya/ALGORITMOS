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
                if self.matrix[i][j] > 0:
                    v += f"{j} "
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

    # busca largura. FILA
    # visita vizinhos do vertice inicial, em seguida os vizinhos do vizinho, funciona com uma fila.
    # vertice inicial v, aciciona v a fila.
    # Enquanto fila nao estiver vazia - reritar primeiro vertice da fila e o marca como visitado (outra lista).
    #                                   - Marca seus vizinhos como visitado e adiciona-os a fila

    def buscaLargura(self, v_inicio) -> list[int]:
        viwed = [v_inicio]
        queue = [v_inicio]

        while len(queue) > 0:
            actual = queue.pop(0)  # remove vertice atual
            # marcar vizinhos como visto
            for i in range(len(self.matrix[actual])):
                vizinho = self.matrix[actual][i]
                if i not in viwed and vizinho > 0:
                    viwed.append(i)
                    queue.append(i)
        return viwed

    def buscaProfundidade(self, v_inicio):
        viwed = []
        stack = [v_inicio]

        while len(stack) > 0:
            actual = stack.pop(len(stack) - 1)  # remove vertice atual do topo da pilha
            if actual not in viwed:
                viwed.append(actual)

                # adicionar vizinhos nao visitados
                for i in range(len(self.matrix[actual])):
                    vizinho = self.matrix[actual][i]
                    if i not in viwed and vizinho > 0:
                        stack.append(i)
        return viwed


# a = Grafo()
# a.addVertice()
# a.addVertice()
# a.addVertice()
# a.linkFromArr(0, [1, 2])
# a.link(2, 1)
# # a.link(1, 1)
# a.showMatrix()
# a.getGraph()
# print(a.getArestasReg(), "Arestas")

print("\n\n\n")
# g3a = Grafo()
# for v in range(11):
#     g3a.addVertice(show=False)

# g3a.linkFromArr(0, [1, 2, 3])
# g3a.linkFromArr(1, [0, 2, 4])
# g3a.linkFromArr(2, [0, 1, 3])
# g3a.linkFromArr(3, [0, 2, 6])

# g3a.linkFromArr(4, [1, 5, 7])
# g3a.linkFromArr(5, [4, 6, 8])
# g3a.linkFromArr(6, [3, 5, 9])

# g3a.linkFromArr(7, [4, 8, 10])
# g3a.linkFromArr(8, [7, 5, 9])
# g3a.linkFromArr(9, [6, 8, 10])

# g3a.linkFromArr(10, [7, 9])  # aq ó
# g3a.showMatrix()
# g3a.getGraph()
# print(g3a.getArestasReg(), "Arestas")


g = Grafo()
for v in range(5):
    g.addVertice(show=False)

g.linkFromArr(0, [1, 3])
g.linkFromArr(1, [0, 2, 4])
g.linkFromArr(2, [1])
g.linkFromArr(3, [0, 4])
g.linkFromArr(4, [1, 3])
g.showMatrix()
g.getGraph()
print(g.getArestasReg(), "Arestas")
print(g.buscaLargura(0))
print(g.buscaProfundidade(0))
