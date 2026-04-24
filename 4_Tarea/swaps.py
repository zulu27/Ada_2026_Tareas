"""
Nombre: César Zuluaga
Codigo: 8989815

"""
from sys import stdin
ans = 0
opt = float('INF')
objetivo = []


def swaps(sol,array):
    global opt,ans,objetivo
    if array == objetivo:
        if sol < opt:
            ans = 1
            opt = sol

        elif opt == sol:
            ans += 1

    elif sol < opt:

        for i in range(0,len(array) - 1):
            #print("prev cam", array)
            
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            #print(array)
                swaps(sol + 1,array)
                array[i], array[i+1] = array[i+1], array[i]

def main():
    line = stdin.readline().strip()
    case = 1
    global ans
    global opt
    global objetivo
    while line != "0":
        array = list(map(int,line.split()))
        array.pop(0)
        ans = 0
        objetivo = list(array)
        objetivo.sort()
        opt = float('INF')

        if not (array == objetivo):
            swaps(0,array)

        print(f'There are {ans} swap maps for input data set {case}.')

        case += 1
        line = stdin.readline().strip() #"0"

main()