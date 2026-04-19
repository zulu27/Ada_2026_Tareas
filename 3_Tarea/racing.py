"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""
from sys import stdin
from heapq import heappop, heappush

INF = float('inf')
grafo= []

def aux_prim(heap,vis,optimo):
    ans = 0
    while len(heap) != 0:
        peso, nodo = heappop(heap)
        if vis[nodo] == False:
            vis[nodo] = True
            ans += peso
            for v,costo in grafo[nodo]:
                costo = costo*-1
                if not vis[v] and costo < optimo[v]:
                    optimo[v] = costo
                    heappush(heap,(costo,v))
        

    return ans    
    

def prim():
    vis = [False for _ in range(len(grafo))]
    optimo = [INF for _ in range(len(grafo))]
    ans = 0
    for nod in range(len(vis)):
        if vis[nod] == False:
            heap = []
            optimo[nod] = -INF
            heappush(heap,(0,nod))
            ans += aux_prim(heap,vis,optimo)
    return ans




def main():
    cases = int(stdin.readline())
    
    for _ in range(cases):
        junctions, roads = map(int,stdin.readline().split())
        res = 0
        for _ in range(junctions):
            grafo.append([])

        for _ in range(roads):
            u,v,costo = map(int,stdin.readline().split())
            res += costo
            u -= 1
            v -= 1
            grafo[u].append((v,costo))
            grafo[v].append((u,costo))
        
        print(res + prim())
        grafo.clear()
        
    stdin.readline()


main()