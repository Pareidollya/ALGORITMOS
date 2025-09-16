import time
import random
import math
from typing import TypeAlias


SortResult: TypeAlias = tuple[list[int], int, str]


def gerar_array(tamanho, limite_min=0, limite_max=100):
    if tamanho > (limite_max - limite_min + 1):
        raise ValueError("Intervalo pequeno demais para gerar números únicos.")
    return random.sample(range(limite_max), tamanho)


original = gerar_array(10000, 0, 1000000)
# original = [53, 63, 26, 2, 57, 72, 52, 79, 46, 92]


def getStrList(results: list[int], show_max=20) -> str:
    result = ""
    for i in results:
        result = result + " " + str(i)
    return result


def showResults(v: list, results: list[SortResult]):
    # print(f"\nArr  :{getStrList(v)}\n")
    print(f"\nArr  :{v}\n")

    for result, time_execution, method in results:
        # getStrList(result)
        print(f"{method}\nResut: {len(result)}\nTime : {time_execution:.6f}\n")


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
def merge_nr(arr: list[int]) -> SortResult:
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

    return conq(original), (ns() - start), "MERGE NAO-RECURSIVO (CAVALOKKKK)"


def merge_nr2(arr: list[int]) -> SortResult:
    start = ns()
    l_size = len(arr) // 2

    # dividir os ultimos ordenando-os
    def swap(swap_arr) -> list[int]:
        a = 0
        while a < (len(swap_arr) - 1):
            if swap_arr[a] > swap_arr[a + 1]:
                swap_arr[a], swap_arr[a + 1] = swap_arr[a + 1], swap_arr[a]
            a += 2
        return swap_arr

    # SIZE BLOCK L = n (conquistado), R <= 2

    def merge_(arr):
        merged = [arr[0]]  # merged
        l, r = 0, 1
        max_r = 2  # tamanho maximo do bloco R pode ir ate 2
        new = []
        while len(merged) < len(arr):
            R = arr[r:max_r]
            # bloco R atual
            if merged[l] <= arr[r]:
                new.append(merged[l])
                l += 1

                if l >= len(merged):  # se L passar e sobrar R, anexa R ao fim
                    new = new + arr[r:max_r]  # adiciona oq sobra de R

                    # avança R para proximo bloco de R
                    r = max_r
                    # avança 2 casas de max r caso seja possivel, senão avança uma
                    max_r = max_r + (2 if max_r + 2 < len(arr) else +1)
                    l = 0
                    merged = new
                    new = []
            else:
                new.append(arr[r])
                r += 1
                # se R passar e sobrar L, anexa L ao fim
                if r >= max_r:
                    new = new + merged[l:]
                    max_r = max_r + (2 if max_r + 2 < len(arr) else +1)
                    l = 0
                    merged = new
                    new = []
        return merged

    return merge_(swap(arr)), (ns() - start), "MERGE NAO-RECURSIVO 2"


# realizar o merge em pares de blocos.. bloco de tamanho 1 merge com bloco de tamanho 2,
# par = bloco1 + bloco2.
# merge = (par[:par/2] + par[par/2:])
# novo par será de de tamanho 4 no arr, com blocos de tamanho 2.
# termina qunado o bloco final for do tamanho da lista
# os não pares se manteem no final da lista. Pois em algum momento será par do bloco maior (haverá 2 blocos)
def merge_nr3(arr: list[int]) -> SortResult:
    start = ns()

    def merge_(left: list[int], right: list[int]):
        r = 0
        l = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # quando terminar é pq sobrou os maiores, so adicionar ao fim caso haja
        result = result + left[l:]
        result = result + right[r:]
        return result

    w = 1  # tamanho do bloco atual
    while w < len(arr):
        # realizar um for em pares esquerda = [i0:w].. esquerda = [i2:w2].. [i4:w4]....
        for i in range(
            w, len(arr), w * 2
        ):  # merge pares (tamanho do bloco) ate o fim do array
            # full bock = w*2, L = w:b/2, R = [b/2 :w]
            left = arr[i - w : i]
            right = arr[i : i + w]
            merged = merge_(left, right)

            arr[i - w : i + w] = merged
        w = w * 2  # dobrar tamanho do bloco pois foram merged
    return arr, (ns() - start), "MERGE NAO-RECURSIVO 3 (based)"


def merge_r(arr: list[int]) -> SortResult:
    start = ns()

    def merge_(left: list[int], right: list[int]):
        r = 0
        l = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # quando terminar é pq sobrou os maiores, so adicionar ao fim caso haja
        result = result + left[l:]
        result = result + right[r:]
        return result

    if len(arr) > 1:
        slice_ = len(arr) // 2
        L, R = arr[:slice_], arr[slice_:]

        arr = merge_(merge_r(L)[0], merge_r(R)[0])
    return arr, (ns() - start), "MERGE RECURSIVO (NOT BASED)"


def quickSort(arr: list[int]) -> SortResult:
    start = ns()

    def partition(
        arr,
    ):  # particionar, colocando menores que pivo na esquerda e maiores na direita
        p = arr[len(arr) - 1]
        i = -1
        for j in range(len(arr)):
            if arr[j] < p:  # caso j seja menor que o pivo
                i += 1  # avança i
                arr[i], arr[j] = arr[j], arr[i]  # swap
            # else incrementa j

        # colocar pivo no centro da lista ao finalizar
        arr[i + 1], arr[j] = arr[j], arr[i + 1]
        return arr, (i + 1)

    if len(arr) >= 1:
        arr_, p = partition(arr)
        # esquerda = [0:p], direita = [p:]
        arr = quickSort(arr_[:p])[0] + [arr[p]] + quickSort(arr_[p + 1 :])[0]

    return arr, (ns() - start), "QUICK SORT"


def countingSort(arr: list[int]) -> SortResult:
    start = ns()
    # get max value
    max_ = arr[0]
    for value in arr:
        if value > max_:
            max_ = value

    # count vector
    count = [0, 0] * max_

    # contagem para posição relativa
    for i in arr:
        count[i] += 1

    result = []
    for num in range(len(count)):
        if count[num] > 0:
            result += [num] * count[num]

    return result, (ns() - start), "COUNTING SORT"


showResults(
    original,
    [
        selection(original.copy()),
        insertion(original.copy()),
        bubble(original.copy()),
        merge_nr(original.copy()),  # insertion hibrido kk
        merge_nr2(original.copy()),
        merge_nr3(original.copy()),  # real merge (based)
        merge_r(original.copy()),
        quickSort(original.copy()),
        countingSort(original.copy()),
    ],
)
