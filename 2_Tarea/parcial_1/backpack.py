"""
Nombre: César A. Zuluaga
Codigo: 8989815
Fecha: 14/03/2026
"""

from sys import stdin


INF = float('inf')
tramos = []
mem = {}


def probar(x):
    ans = 0
    acum = 0
    for i in tramos:
        if acum + i <= x:
            acum += i
        
        else:
            acum = i
            ans += 1
    return ans
    

def backpack(l,r,d):
    if l >= r:
        ans = l
    
    else:
        mit = l + ((r-l) >> 1)
        aux = probar(mit)
        if aux <= d:
            ans = backpack(l,mit,d)
        else:
            ans = backpack(mit + 1,r,d)


    return ans



def main():

    line = stdin.readline()

    while line != "":
        camps, days = map(int,line.split())

        sum_tramos = 0
        maximo = 0
        for _ in range(camps + 1):
            c = int(stdin.readline())
            tramos.append(c)
            maximo = max(c,maximo)
            sum_tramos += c
        ans = backpack(maximo,sum_tramos,days)

        print(ans)

        tramos.clear()
        mem.clear()
        line = stdin.readline()

main()