#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 02/03/2026

from sys import stdin
import sys

# 2. Incrementar el límite (por ejemplo, a 2000)
sys.setrecursionlimit(1000000)
pizzas = {}

llaves = {}


def topo():
    inc, queue, topo = [0 for _ in range(len(pizzas))], deque(), []
    for v in pizzas:
        for u in pizzas[v]:
            inc[u] += 1

    for v in inc:
        if v == 0:
            queue.append(v)
            

    while len(queue) > 0:
        v = queue.popleft()
        topo.append(v)
        for u in pizzas[v]:
            inc[v] -= 1
            if inc[v] == 0:
                queue.append(v)

    return topo


def main():
    line = stdin.readline()

    while line != "":
        costo = int(line)
        recepie = int(stdin.readline())
        i = 0
        for _ in range(recepie):
            
            derivado, base, _, euro, prestige = stdin.readline().split()
            euro = int(euro)
            prestige = (int(prestige))

            if base not in llaves:
                llaves[base] = i
                i += 1
            
            if derivado not in llaves:
                llaves[derivado] = i
                i += 1

            pizzas[llaves[base]].append([llaves[derivado],euro,prestige])

        historic_prestige = 0
        historic_price = float('inf')

        topo = topo()

        for key in bases:
            prestige, price = pizza(key,costo)

            if price < historic_price:
                historic_price = price
                historic_prestige = prestige

            elif historic_prestige < prestige and price == historic_price:                 
                historic_price = price
                historic_prestige = prestige

        print(historic_prestige)
        print(historic_price)
        print(pizzas)
        pizzas.clear()
        bases.clear()
        derivados.clear()
        line = stdin.readline()





main()