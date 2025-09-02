import time
import math
from typing import TypeAlias

original = [
    64,
    25,
    12,
    22,
    11,
    5,
    2,
    7,
    9,
    3,
    5,
    # 78,
    # 0,
]

SortResult: TypeAlias = tuple[list[int], int, str]


def getStrList(results: list[int]) -> str:
    result = ""
    for i in results:
        result = result + " " + str(i)
    return result


def showResults(v: list, results: list[SortResult]):
    print(f"\nArr  :{getStrList(v)}\n")
    for result, time_execution, method in results:
        print(f"{method}\nResut:{getStrList(result)}\nTime : {time_execution:.6f}\n")


def ns() -> int:
    return time.perf_counter()


def selection(arr: list[int]) -> SortResult:
    start = ns()
    pos = 0
    for a in arr:
        # buscar menor valor do array
        index = pos
        min_index = index
        for i in arr[pos:]:
            if i < arr[min_index]:
                min_index = index
            index += 1
        # swap
        arr[pos], arr[min_index] = arr[min_index], a
        pos += 1
    return arr, (ns() - start), "SELECTION"


def insertion(arr: list[int]) -> SortResult:
    start = ns()
    pos = 0
    for a in arr[pos + 1 :]:  # inicia do segundo elemento assumindo ja estar ordenado
        # pos+1 = actual key pos
        # percorrer esse subarray verificando se o valor atual está ordenado
        # avança, comparando o elemento atual com os 2 anteriores e swapa-lo na posição correta
        pos_b = 0
        for b in arr[: pos + 1]:
            if a < b:
                arr[pos_b], arr[pos + 1] = arr[pos + 1], arr[pos_b]
            pos_b += 1
        pos += 1

    return arr, (ns() - start), "INSERTION"


def bubble(arr: list[int]) -> SortResult:
    start = ns()
    for a in range(len(arr)):
        for b in range(len(arr)):
            if arr[b] > arr[a]:
                # swap
                arr[a], arr[b] = arr[b], arr[a]
    return arr, (ns() - start), "BUBBLE"


# merge bruto sem recursao da silva
def merge(arr: list[int]) -> SortResult:
    start = ns()

    l_size = len(arr) // 2
    r_size = len(arr[l_size:])  # slice start index

    # dividir
    L = arr[:l_size]
    R = arr[r_size - 1 :]

    def swap(swap_arr):  # TODO: tem q fazer um swap-back para estar tudo ordenado
        for a in range(len(swap_arr) - 1):
            if swap_arr[a] > swap_arr[a + 1]:
                swap_arr[a], swap_arr[a + 1] = swap_arr[a + 1], swap_arr[a]
        return swap_arr

    def merge(arr_l, arr_r):
        merged = []

        l = 0
        r = 0
        while r < len(arr_r):
            # verificar se sobrou, quanto sobrou e adiciona-los a lista
            if l > len(arr_l):  # é pq acabou l, adiciona sobra de r
                merged.append(arr_r[r + 1])
                break
            elif r > len(arr_r):
                merged.append(arr[l + 1])
                break

            if arr_l[l] > arr_r[r]:
                merged.append(arr_r[r])
                r += 1
            else:
                merged.append(arr_l[l])
                l += 1
        # adicionar oq sobrar
        if l < len(arr_l) - 1:
            for l_ in arr_l[l:]:
                merged.append(l_)
        if r < len(arr_r) - 1:
            for r_ in arr_r[r:]:
                merged.append(r_)

        return merged

    L = swap(L)
    R = swap(R)
    # first swaps

    return merge(L, R), (ns() - start), "MERGE NAO-RECURSIVO"


showResults(
    original,
    [
        selection(original.copy()),
        insertion(original.copy()),
        bubble(original.copy()),
        merge(original.copy()),
    ],
)
