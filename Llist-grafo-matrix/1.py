# linked-list classes
from typing import Generic, TypeVar
import copy
import random

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T = None, next_node=None, previous_node=None, index=0):
        self.value = value or None
        self.next_node: Node[T] = next_node
        self.previous_node: Node[T] = previous_node
        self.index = index


class LinkedList(Generic[T]):
    def __init__(self, head: Node[T] = None, tail: Node[T] = None, len_=0):
        self.head = head
        self.tail = tail
        self.len = len_
        pass

    def add(self, value: T, fromHead=False, log=True):

        node = Node()
        node.value = value
        # insert na head
        if self.head == None or fromHead:
            print(f"{node.value} added as head, index {node.index}") if log else ""

            node.next_node, self.head = self.head, node

            # if self.head.next_node:  # Deus eh mais...
            #     fix_index = 1
            #     actual = self.head
            #     while actual.index == 0:
            #         self.head.next_node = fix_index
            #         fix_index += 1
            #         if actual.next_node == None:
            #             break
            #         actual = actual.next_node

        # percorrer de head ate final
        else:
            actual = self.head
            while actual.next_node != None:
                actual = actual.next_node
            node.index = actual.index + 1
            actual.next_node = node
            print(f"{value} added, index {node.index}") if log else ""
        self.len += 1

    def getList(self) -> list[T]:
        node = self.head
        list_ = []
        while node != None:
            # list_ = list_ + f"{node.value}{', ' if node.next_node != None else ''}"
            list_.append(node.value)
            node = node.next_node

        return list_

    def get(self, index: int) -> Node[T]:
        node = self.head
        while node != None:
            if node.index == index:
                return node
            else:
                node = node.next_node
        return None

    def getSegundoMenorkk(
        self, optmize=True, sort_original_arr=False
    ):  # tanka essa pra pegar segundo menor mas sem ordenar original
        list_ = self if sort_original_arr else copy.deepcopy(self)
        actual = list_.head  # percorrer apartir do inicio
        gamer_optimization = 0
        while actual != None and gamer_optimization < (list_.len if not optmize else 2):
            next_ = actual.next_node
            min_node = actual
            while next_ != None:  # percorrer a partir do atual buscando um menor
                if next_.value <= min_node.value:
                    min_node = next_
                next_ = next_.next_node

            # swap node values
            actual.value, min_node.value = min_node.value, actual.value
            actual = actual.next_node  # next node
            gamer_optimization += 1
        return list_

    def sequancialSerach(self, value: T):  # retornar os index que aparecem valor X
        actual = self.head
        positions = []
        index = 0
        while actual != None:
            if actual.value == value:
                positions.append(index)

            actual = actual.next_node
            index += 1
        return positions

    def addFromArr(self, arr: T, fromHead=False, log=True):
        for i in arr:
            self.add(i, fromHead=fromHead, log=log)


print("\n\n")
a = LinkedList[int](head=None, tail=None)

# inserção na cabeça
a.addFromArr([0, 1, 2, 26], fromHead=True)
print(a.getList())

# inserção no final
a.addFromArr([53, 63, 26, 57, 72, 52, 46, 26, 92, 91])

print("arr", a.getList())

# segundo menor elemento no arr
menores = a.getSegundoMenorkk(optmize=True, sort_original_arr=False).getList()
print(f"\nsegundo menor elemento é {menores[1:][0]}")


# busca sequencial de valor X
vts = 26
search_result = a.sequancialSerach(vts)
print(
    f"O valor {vts} apararece {len(search_result)} vez(es), nas posições {search_result}"
)


# soma de duas marizes quadradas. Nivel autism 2 😈👹
def gen_arr(size, minLimit=0, maxLimit=10):
    if size > (maxLimit - minLimit + 1):
        raise ValueError("intervalo piqueno di mais :/")
    return random.sample(range(minLimit, maxLimit + 1), size)


# show matrix
def getLinkedMatrix(m: LinkedList[LinkedList[int]], show=True):
    final_matrix = []
    a = m.head
    while a != None:  # linha = lista 0, lista 1, ....
        # print("linha1", a.value)
        b = a.value.head  # NODE, COLUNA
        aksldj = []
        while b != None:
            # print(f"{b.value}, ", end="")
            aksldj.append(b.value)
            b = b.next_node
        final_matrix.append(aksldj)
        a = a.next_node

    if show:
        for i in final_matrix:
            print(i)
    return final_matrix


# somar matrizes [0][0] + [0][0], [1][0] + [1][0],.... coluna 0 + coluna 0, ....
def sumLinkedMatrix(m1: LinkedList[LinkedList[int]], m2: LinkedList[LinkedList[int]]):
    final_matrix = LinkedList[LinkedList[int]]()
    a, b = m1.head, m2.head
    while a != None:
        col_a, col_b = a.value.head, b.value.head
        new_line = LinkedList[int]()
        while col_a != None:
            sum_ = col_a.value + col_b.value
            new_line.add(sum_, log=False)
            col_a, col_b = col_a.next_node, col_b.next_node  # avançar proximas colunas

        final_matrix.add(new_line, log=False)
        a, b = a.next_node, b.next_node
    return final_matrix


n = 2  # tamanho e numero de linhas (quadratico)
matrix1, matrix2 = LinkedList[LinkedList[int]](), LinkedList[LinkedList[int]](
    head=None, tail=None
)
for i in range(n):  # gen matrix² por ma vontade msm
    arr = []
    linha1, linha2 = LinkedList[int](), LinkedList[int]()
    for j in range(n):
        # linha
        arr1, arr2 = gen_arr(n), gen_arr(n)
        linha1.addFromArr(arr1, log=False), linha2.addFromArr(arr2, log=False)

    matrix1.add(linha1, log=False), matrix2.add(linha2, log=False)

print("\nLinked Matrix o_O")
print("matrix1", getLinkedMatrix(matrix1, show=False))
print("matrix2", getLinkedMatrix(matrix2, show=False))
print("sum matrix", getLinkedMatrix(sumLinkedMatrix(matrix1, matrix2), show=False))

# busca sequencial

#  O intervalo de um conjunto finito e não vazio de números reais S é definido como
#  a diferença entre o maior e o menor elementos de S. Para cada representação de S
#  abaixo elabore um algoritmo para computar o intervalo e calcule a complexidade
#  destes algoritmos.
#  a) um vetor ordenado
#  b) um vetor desordenad

S = gen_arr(maxLimit=11, minLimit=1, size=10)
x = LinkedList()
x.addFromArr(S, log=False)
# menor e maior (desordenado)

actual = x.head
min_ = x.head
max_ = x.head
while actual != None:

    if actual.value <= min_.value:
        min_ = actual
    elif actual.value > max_.value:
        max_ = actual

    actual = actual.next_node
print("\n\narr unsorted", x.getList())
print(f"diff ({min_.value}, {max_.value}) { max_.value - min_.value  } ")
# ordenado

x2 = x.getSegundoMenorkk(optmize=False, sort_original_arr=False)


print("sorted", x2.getList())
print(
    "diferença é (sorted): ", x2.get(x.len - 1).value - x2.get(0).value
)  # primeiro - ultimo valor O(n)
# diff =
