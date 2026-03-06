#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 02/03/2026

from sys import stdin
import sys
from collections import deque
# 2. Incrementar el límite (por ejemplo, a 2000)
sys.setrecursionlimit(1000000)
pizzas = {}
llaves = {}
fuentes = []
memoria = {}


def topo():
    inc, queue, topo = [0 for _ in range(len(pizzas))], deque(), []
    for v in pizzas:
        for u in pizzas[v]:
            inc[u[0]] += 1

    for v in range(len(inc)):
        if inc[v] == 0:
            queue.append(v)
            fuentes.append(v)
            

    while len(queue) > 0:
        v = queue.popleft()
        topo.append(v)
        for u in pizzas[v]:
            inc[u[0]] -= 1
            if inc[u[0]] == 0:
                queue.append(u[0])

    return topo

def calc_mincost(topito):
    val = [[float('inf'),0] for _ in range(len(pizzas))]
 
    for v in fuentes:
        val[v][0] = 0
        val[v][1] = 0


    for v in topito:
        
        for u, c, p in pizzas[v]:

            if val[u][0] > val[v][0] + c:
                val[u][0] = val[v][0] + c
                val[u][1] = val[v][1] + p

            elif val[u][0] == val[v][0] + c and val[u][1] < val[v][1] + p:
                val[u][0] = val[v][0] + c
                val[u][1] = val[v][1] + p

    return val

def max_benf(n,capacidad,val):
    ans = [0,0]

    if (n,capacidad) in memoria:
        ans = memoria[(n,capacidad)]

    elif n == len(val):
        ans[0] = 0 #costo
        ans[1] = 0 #prestigio

    else:
        elegir = []
        if capacidad - val[n][0] >= 0:
            elegir = max_benf(n + 1,capacidad - val[n][0],val)
            elegir[0] += val[n][0]
            elegir[1] += val[n][1]

        no_elegir = max_benf(n + 1, capacidad,val)
        

        if elegir != []:
            if elegir[1] > no_elegir[1]:
                ans = elegir

            elif elegir[1] == no_elegir[1]:
                costo_min = min(elegir[0],no_elegir[0])
                ans = [costo_min,elegir[1]]
            else:
                ans = no_elegir
        
        else:
            ans = no_elegir
        
        memoria[(n,capacidad)] = ans

    return ans
"""

def max_benf(n,capacidad,val,costo):
    ans = 0


    if n < len(val) and capacidad > 0:

        elegir = 0
        if capacidad - val[n][0] >= 0:
            elegir = max_benf(n + 1,capacidad - val[n][0],val,costo) + val[n][1]


        no_elegir = max_benf(n + 1, capacidad,val,costo)
       #print(val[n][0],val[n][1])
        print(elegir,no_elegir)
        if elegir != 0:
            if elegir > no_elegir:
                ans = elegir
            else:
                ans = no_elegir
        
        else:
            ans = no_elegir

 

    return ans
"""

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


            if llaves[base] not in pizzas:
                pizzas[llaves[base]] = []

            if llaves[derivado] not in pizzas:
                pizzas[llaves[derivado]] = []
            

            pizzas[llaves[base]].append([llaves[derivado],euro,prestige])

        
        topito = topo()
        val = calc_mincost(topito)
        

        ans = max_benf(0,costo,val)

        #print(ans)
        print(ans[1])
        print(ans[0])
        pizzas.clear()
        llaves.clear()
        topito.clear()
        memoria.clear()
        fuentes.clear()
        val.clear()
        line = stdin.readline()





main()