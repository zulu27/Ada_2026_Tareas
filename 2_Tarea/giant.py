#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 01/03/2026

from sys import stdin

memorizacion = {}

def giant(left,right,k):
    if left == right or left > right:
        ans = 0

    elif (left,right) in memorizacion:
        ans = memorizacion[left,right]

    else:
        ans = float('inf')
        
        for i in range(left,right + 1):

            #es sour
            costo = giant(left, i - 1,k)
            #es bitter
            costo += giant(i + 1,right,k)
            #costo de elegir esa manzana
            costo += ((right - left) + 1)*(i + k)

            ans = min(ans,costo)

        memorizacion[left,right] = ans

    return ans


def main():
    cases =int(stdin.readline())

    for i in range(cases):

        n, k = map(int,stdin.readline().split())

        ans = giant(1,n,k)

        print(f'Cases {i + 1}: {ans}')


main()