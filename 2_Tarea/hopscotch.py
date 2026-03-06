#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 26/02/2026


from sys import stdin
square_grid = [[0 for _ in range(100)] for _ in range(100)]
memoria = {}

def up(p,q,n,k):
    ans = 0
    aux = 0
    for i in range(k):

        if  (p - (i + 1)) >= 0 and square_grid[p][q] < square_grid[p - (i + 1)][q]:

            aux = hopscotch(p-(i + 1),q,n,k)
            if aux > ans:
                ans = aux

    return ans

def down(p,q,n,k):
    ans = 0
    aux = 0
    for i in range(k):
        if (p + (i + 1)) < n and square_grid[p][q] < square_grid[p + (i + 1)][q]:
            aux = hopscotch(p+(i + 1),q,n,k)
            if aux > ans:
                ans = aux
    return ans

def left(p,q,n,k):
    ans = 0
    aux = 0

    for i in range(k):

        if (q - (i + 1)) >= 0 and square_grid[p][q] < square_grid[p][q - (i + 1)]:
            aux = hopscotch(p,q-(i + 1),n,k)
            if aux > ans:
                ans = aux

    return ans

def right(p,q,n,k):
    ans = 0
    aux = 0

    for i in range(k):
        if ( q + (i + 1)) < n and square_grid[p][q] < square_grid[p][q + (i + 1)]:
            aux = hopscotch(p, q + (i + 1), n, k)
            if aux > ans:
                ans = aux
    return ans

def hopscotch(p,q,n,k):
    ans = 0

    if (p,q) not in memoria:

        u = up(p,q,n,k)
        d = down(p,q,n,k)
        l = left(p,q,n,k)
        r = right(p,q,n,k)
        ans = max(u,d,l,r)


        memoria[(p,q)] = ans + square_grid[p][q]


    return memoria[(p,q)]



def main():
    cases = int(stdin.readline())

    for a in range(cases):
        stdin.readline()
        n , k = map(int,stdin.readline().split())

        for i in range(n):
            values = list(map(int,stdin.readline().split()))
            for j in range(len(values)):
                square_grid[i][j] = values[j]

        ans = hopscotch(0,0,n,k)
        
        if a != (cases - 1):
            print(f'{ans}\n')

        else:
            print(f'{ans}')

        memoria.clear()

        for i in range(n):
            for j in range(n):
                square_grid[i][j] = 0


main()