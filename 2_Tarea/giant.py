#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 01/03/2026

from sys import stdin
INF = float('inf')

def giant_tabulacion(n,k):
    tab = [[0 for _ in range(n + 1)] for _ in range(n + 1) ]
    r = 1
    while r < (n + 1):
        l = r - 1
        while l > 0:
            i = l
            histo = INF
            while i < r:
                peso = tab[l][i - 1]
                peso += tab[i + 1][r]
                peso += ((r - l) + 1) * ((i) + k)
                histo = min(peso,histo)

                i += 1


            tab[l][r] = histo
            l -= 1
        r += 1
    return tab[1][n] 





def main():
    cases =int(stdin.readline())

    for i in range(cases):

        n, k = map(int,stdin.readline().split())
        ans = giant_tabulacion(n,k)
        print(f'Case {i + 1}: {ans}')

main()