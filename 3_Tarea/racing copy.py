"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""
from sys import stdin
from heapq import heappop, heappush
from collections import deque
candidatos = {}
grafo = []
class Aristas:
    def __init__(self,u,v,costo):
        self.u = u
        self.v = v
        self.c = costo

    def getArista(self):
        return (self.u,self.v,self.c)
    
    def __lt__(self,other):
        return self.c > other.c

def bfs(junctions):
    padre = [-1 for _ in range(junctions)]
    vis = [0 for _ in range(junctions)]
    cola = deque()
    cola.append(0)
    padre[0] = 0
    


    while len(cola) != 0:
        nodo = cola.popleft()
        vis[nodo] = 1
        for v, _ in grafo[nodo]:
            if vis[v] == 0:
                vis[v] = 1
                cola.append(v)
                padre[v] = nodo

            elif padre[nodo] != v:
                a,b = min(nodo,v), max(nodo,v)
                candidatos[a,b] += 1



def main():
    cases = int(stdin.readline())
    
    for _ in range(cases):
        junctions, roads = map(int,stdin.readline().split())
        aristas = []
        for i in range(junctions):
            
            grafo.append([])

        for i in range(roads):
            u,v,cost = map(int,stdin.readline().split())
            a, b = min(u-1, v-1), max(u-1, v-1)
            candidatos[(a, b)] = 0
            grafo[u-1].append(v-1,cost)
            grafo[v-1].append(u-1,cost)
            
        bfs()
        
        aristas.sort(junctions)

       

        ans = racing()

        
    stdin.readline()
    

    


main()