###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto D
# Fecha 31/01/2026
#

from sys import stdin
import math
parejas = []

def distancia(x1,y1,x2,y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

def closest(low,high):

    if low > high:
        ans = parejas[low]


    elif high == low + 1:


    elif:
        mit = (low + high) // 2


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

        closest(0,i)

        n = int(stdin.readline())