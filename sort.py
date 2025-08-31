import time
from typing import TypeAlias, Callable

arr = [64, 25, 12, 22, 11]

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


def selection(arr_: list[int]) -> SortResult:
    start = ns()
    pos = 0
    for a in arr_:
        h = {"value": a, "pos": pos}
        l = {"value": 99999, "pos": 0}

        # buscar menor valor do array
        index = pos
        for i in arr_[pos:]:
            if i < l["value"]:
                l = {"value": i, "pos": index}
            elif i > h["value"]:
                h = {"value": i, "pos": index}
            index += 1
        # swap
        arr_[pos], arr_[l["pos"]] = l["value"], a
        pos += 1
    return arr_, (ns() - start), "SELECTION"


s = selection(arr.copy())
showResults(arr, [s])
