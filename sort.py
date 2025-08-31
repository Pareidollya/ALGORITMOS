import time
from typing import TypeAlias, Callable

arr = [3, 2, 1, 0]

SortResult: TypeAlias = tuple[list[int], int, str]


def getStrList(results: list[str]) -> str:
    result = ""
    for i in results:
        result = result + " " + str(i)
    return result


def showResults(v: list, results: list[SortResult]):
    print(f"\nArr  :{getStrList(arr)}\n")
    for result, time_execution, method in results:
        print(f"{method}\nResut:{getStrList(result)}\nTime : {time_execution}\n")


a: SortResult = [(arr, 1, "teste")]

showResults(arr, a)
