###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto D
# Fecha 31/01/2026
#

from sys import stdin
import math
parejas = []

def distancia(dl,dr):
    x1 = dl[0]
    y1 = dl[1]
    x2 = dr[0]
    y2 = dr[1]
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

def closest(low,high):

    if high - low == 2:
        ans = distancia(parejas[low],parejas[low + 1])

    elif high - low == 3:
        d1 = distancia(parejas[low],parejas[low + 1])
        d2 = distancia(parejas[low],parejas[low + 2])
        d3 = distancia(parejas[low+2],parejas[low + 1])
        ans = min(d1,d2,d3)

    else:
        mit = low + ((high-low) >> 1 )

        d1 = closest(low,mit)
        d2 = closest(mit,high)
        ans = min(d1,d2)

        s = []

        while A[mit][0] 





    return ans

def main():
    n = int(stdin.readline())

    while n > 0:
        i = 0
        for _ in range(n):
            a,b = map(int,stdin.readline().split())
            parejas.append((a,b))
            if i < a:
                i = a
        parejas.sort()

        ans = closest(0,len(parejas))

        n = int(stdin.readline())