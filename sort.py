import time
import math
from typing import TypeAlias

original = [64, 25, 22, 12, 11, 5, 7, 3, 31, 57, 89, 10]

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
    max_it = l_size

    # dividir
    L = arr[:l_size]
    R = arr[l_size:]

    # first swaps
    def swap(swap_arr):
        a = 0
        while a < (len(swap_arr) - 1):
            if swap_arr[a] > swap_arr[a + 1]:
                swap_arr[a], swap_arr[a + 1] = swap_arr[a + 1], swap_arr[a]
            a += 2
        return swap_arr

    L = swap(L)
    R = swap(R)

    # CONQUEEEEEEEEEEER
    # FOR LEN / 2 ( aumentando array e ir conquistando essa poha)
    def conq(arr):
        final_arr = []
        # os primeiros ja estarão ordenados
        # aumentando o tamanho do bloco principal e reduzindo dos proximos
        # comparar o primeiro elemento do principal com o primeiro do proximo bloco

        conquested = [arr[0]]
        l, r = 0, 1
        atual = 0
        while len(conquested) < len(
            arr
        ):  # aumentou area conquistada ate se igualar ao tamanho total

            new_conquested = []
            appends = 0
            while atual < len(
                conquested
            ):  # TODO SO PRECISA ADICIONAR UM POR VEEEEEEEEEEEEEEEEEZ PERCORRENDO OS JA CONQUISTADO E INSERIR NA POSIÇÃO CORRETA
                # basicamente focar em reescrever conquest com a posição correta

                if conquested[atual] > arr[r]:  # se o proximo for menor que o atual
                    new_conquested.append(arr[r])  # adiciona o proximo antes do atual
                    conquested = (
                        conquested[:atual] + new_conquested + conquested[atual:]
                    )
                    r += 1  # avança proximo
                    atual = 0
                    break

                elif conquested[atual] < arr[r]:  # se atual for menor que o proximo
                    # new_conquested.append(conquested[atual])  # adiciona o atual

                    if (
                        atual < len(conquested) - 1
                    ):  # se o atual nao for o ultimo da lista avança o atual
                        # pra comparar o proximo atual com r
                        atual += 1
                        break

                    conquested = (
                        conquested[: atual + 1] + [arr[r]] + conquested[atual + 1 :]
                    )

                    r += 1
                    atual = 0
                    break

                if appends > len(
                    conquested
                ):  # se houver mais adiçoes que a lista atual adicionar quem sobra de conquest a partir do atual no final
                    new_conquested.append(arr[r])
                    conquested = new_conquested + conquested[atual:]
                    break

                if atual == len(
                    conquested
                ):  # se nao tiver um proximo atual adiciona proximo ao fim
                    new_conquested.append(arr[r])
                    r += 1
                    conquested = new_conquested
                    break

        return conquested

    return conq(L + R), (ns() - start), "MERGE NAO-RECURSIVO (CAVALOKKKK)"


showResults(
    original,
    [
        selection(original.copy()),
        insertion(original.copy()),
        bubble(original.copy()),
        merge(original.copy()),
    ],
)
