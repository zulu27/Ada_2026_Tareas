"""
Nombre: César A. Zuluaga
Codigo: 8989815
Fecha: 14/03/2026
"""

from sys import stdin

routes = []
mem = {}


def fry(n,c):
    c = min(c,len(routes) - n)
    key = (n,c)

    if  n == len(routes):
        ans = 0

    elif key in mem:
        ans = mem[key]

    else:
        if c > 0:
            ans = min(fry(n+1,c+routes[n][1] - 1)+ routes[n][0]//2, fry(n+1,c+routes[n][1]) + routes[n][0])
        
        else:
            ans = fry(n+1,c+routes[n][1]) + routes[n][0]

    mem[key] = ans


    return ans




def main():
    n = int(stdin.readline())

    while n != 0:
        
        for _ in range(n):
            t, b = map(int,stdin.readline().split())

            routes.append((t,b))

        
        ans = fry(0,0)

        print(ans)

        routes.clear()
        mem.clear()

        n = int(stdin.readline())
main()