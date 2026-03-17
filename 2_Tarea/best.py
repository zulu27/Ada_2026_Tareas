#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 26/02/2026

from sys import stdin

stocks =  []
memoria = {}
INF = float('inf')

def best(n,c):
    key = (n,c)

    ans = INF

    if key in memoria:
        ans = memoria[key]

    elif c <= 0:
        ans = 0

    elif n == len(stocks):
        ans = INF
    
    else:
        elegir = best(n+1,c - stocks[n]) + stocks[n]
        no_elegir = best(n+1,c)
        if elegir != INF and no_elegir != INF:

            if elegir >= c and no_elegir >= c:
                ans = min(elegir,no_elegir)

            elif elegir >= c:
                ans = elegir

            elif no_elegir >= c:
                ans = no_elegir

            else:
                ans = max(no_elegir,elegir)

        elif elegir != INF:
            ans = elegir
        
        elif no_elegir != INF:
            ans = no_elegir

        else:
            ans = INF

    memoria[key] = ans

    return ans


def main():

    cases, holder = map(int,stdin.readline().split())
    j = 1
    while cases != 0 and holder != 0:
        holder -= 1
        
        for i in range(cases):
            porcentaje = round(float(stdin.readline()) * 100)


            if i == holder:
                porcentage_holder = porcentaje

            else:
                stocks.append(porcentaje)

        ans = best(0,5001 - porcentage_holder) + porcentage_holder
        ans = (porcentage_holder*100)/ans


        print(f'{ans:.2f}')

        
        memoria.clear()
        cases, holder = map(int,stdin.readline().split())

        stocks.clear()
        j += 1

main()