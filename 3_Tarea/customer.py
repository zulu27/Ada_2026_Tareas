"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""
from sys import stdin
from heapq import heappop, heappush
fechas = []

def customer():
    elegidos = []
    tiempo_total = 0
    for fecha, tiempo in fechas:
        if tiempo_total + tiempo <= fecha:
            tiempo_total += tiempo
            heappush(elegidos,-tiempo)
  

        elif len(elegidos) != 0 and tiempo_total + elegidos[0] + tiempo <= fecha and tiempo  < -elegidos[0]:
            tiempo_total = tiempo_total + elegidos[0] + tiempo
            heappop(elegidos)
            heappush(elegidos,-tiempo)

        
    return len(elegidos)

def main():
    cases = int(stdin.readline())
    stdin.readline()
    for _ in range(cases):
        entregas = int(stdin.readline())
        for _ in range(entregas):
            tiempo, final = map(int,stdin.readline().split())
            fechas.append((final,tiempo))

        stdin.readline()
        fechas.sort()
        ans = customer()
        print(ans)
        print()
        fechas.clear()

main()