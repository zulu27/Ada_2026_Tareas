
'''
Solution E - Racing
Daniel Alejandro Posada Noguera
25 de Marzo del 2026
'''

from sys import stdin
from collections import deque
from heapq import heappush, heappop

n, m, s_weights, INF = int(), int(), int(), float('inf')
graph = [[] for _ in range(10000)]
d, vis = [INF] * 10000, [False] * 10000

def prim_cameras():
    global n, m, s_weights, graph, d, vis
    pq, total, flag = [], s_weights, False
    d[0] = 0; heappush(pq, (0, 0))

    while len(pq) > 0:
        du, u = heappop(pq)
        if du == d[u] and not vis[u]:
            vis[u] = True
            total += du
            for (dv, v) in graph[u]:
                if not vis[v] and -dv < d[v]:
                    d[v] = -dv
                    heappush(pq, (-dv, v))
    return total

def solve():
    global vis
    s = prim_cameras()
    print(s)

def main():
    global n, m, s_weights, graph, d, vis
    cases = int(stdin.readline())
    for _ in range(cases):
        n, m = map(int, stdin.readline().split())
        s_weights = 0
        for i in range(n): 
            vis[i] = False; d[i] = INF
            graph[i].clear()
        for i in range(m):
            u, v, c = map(int, stdin.readline().split())
            s_weights += c
            graph[u - 1].append((c, v - 1))
            graph[v - 1].append((c, u - 1))
        solve()

main()