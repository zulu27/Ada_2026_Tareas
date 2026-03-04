#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 26/02/2026

from sys import stdin

stocks =  []
memoria = {}

def best(n,c):
    if n == len(stocks):
        ans = 0
    
    elif (n,c) in memoria:
        ans = memoria[(n,c)]
    else:
        elegir = best(n+1,c - stocks[n]) + stocks[n]
        no_elegir = best(n+1,c)

        if c - elegir <= 0 and c - no_elegir <= 0:
            ans = min(elegir,no_elegir)
        
        elif c - elegir > 0 and c - no_elegir > 0:
            ans = max(elegir,no_elegir)
        
        elif c - elegir <= 0: 
            ans = elegir
        
        else:
            ans = no_elegir
        
        memoria[(n,c)] = ans

    return ans

def main():

    cases, holder = map(int,stdin.readline().split())

    while cases != 0 and holder != 0:
        holder -= 1
        
        for i in range(cases):
            porcentaje = float(stdin.readline())


            if i == holder:
                porcentage_holder = porcentaje

            else:
                stocks.append(porcentaje)

        ans = best(0,50 - porcentage_holder) + porcentage_holder

        ans = (porcentage_holder*100)/ans

        print(f'{round(ans,2):.2f}')
        stocks.clear()
        memoria.clear()
        cases, holder = map(int,stdin.readline().split())

main()