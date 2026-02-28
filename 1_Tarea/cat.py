###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto A
# Fecha 31/01/2026
#

from sys import stdin
import math


def probar_n(k,workers):
    bottom = 1
    top = workers
    while bottom < top:
        mit = (top + bottom) // 2

        if (mit**k) == workers:
            bottom = mit
            top = 0

        elif (mit**k) < workers:
            bottom = mit + 1

        else:
            top = mit

    return bottom

def calculo_nivel(tallest,workers):
    k = 1
    ans = []
    while k < int(math.log2(tallest)) and len(ans) == 0:
        res = probar_n(k,workers)

        if (res**k) == workers and ((res + 1)**k) == tallest:
            ans = [res,k]

        k += 1

    return ans

def calc_final(n,k,tallest,workers):
    i = 0
    no_trabaja = 0
    altura = 0

    while i <= k:
        if i < k:
            no_trabaja += n**i
        altura += (n**i) * ((n + 1)**(k - i))

        i += 1

    return [no_trabaja,altura]


def main():

    tallest, workers = map(int, stdin.readline().split())
    l = [0,0]

    while tallest != 0 and workers != 0:
        if tallest == 1 and workers == 1:
            l[0] = 0
            l[1] = 1

        else:

            ans = calculo_nivel(tallest,workers)
            l = calc_final(ans[0],ans[1],tallest,workers)


        print(l[0],l[1])

        tallest, workers = map(int, stdin.readline().split())




main()