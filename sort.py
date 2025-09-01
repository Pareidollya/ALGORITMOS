import time
from typing import TypeAlias

original = [64, 25, 12, 22, 11]

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


showResults(
    original,
    [selection(original.copy()), insertion(original.copy()), bubble(original.copy())],
)
