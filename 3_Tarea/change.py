"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""
from sys import stdin
import copy
INF = float('inf')
monedas = [5,10,20,50,100,200]
 
def pasarme(vuelto):
    ans = 0
    i = 5

    while vuelto > 0 and i >= 0:
        #print(ans,vuelto,monedas[i])
        #print(i)
        if vuelto >= monedas[i]:
            vuelto -= monedas[i]
            ans += 1
        
        else:
            i -= 1

    if vuelto != 0:
        ans = INF

    return ans

def calc_combo(valor, cantidad_monedas):
    ans = 0
    i = 5
    while valor > 0 and i > -1:
        if cantidad_monedas[i] != 0 and valor >= monedas[i]:
            valor -= monedas[i]
            ans += 1 
            cantidad_monedas[i] -= 1
            
            if cantidad_monedas[i] == 0 :
                i -= 1
        else:
            i -= 1    

    if valor > 0:
        ans = INF
    
    return ans



def change(cantidad_monedas,factura,candidatos):
    ans = INF

    for valor in candidatos:
        
        monedas = calc_combo(valor,copy.deepcopy(cantidad_monedas))
        vuelto = pasarme(valor - factura)

        ans = min(ans,monedas + vuelto)
    
    return ans


def main():
    cantidad_monedas = list(map(float,stdin.readline().split()))
    i = 0
    while(len(cantidad_monedas)) != 6:
        #print(cantidad_monedas[-1]," factura")
        factura = int(round(cantidad_monedas[-1]*100))
    
        i = 0
        flag = False
        posibles_valores = []
        while not flag:
            if cantidad_monedas[i] != 0:
                flag = True
            else:
                i += 1

        
        maximo = 200 + factura

        valor = factura
        while valor < maximo:
            posibles_valores.append(valor)
            valor += monedas[0]
        posibles_valores.append(maximo)
        

        ans = change(cantidad_monedas,factura,posibles_valores)
        
        print(f"{ans:3d}")

        cantidad_monedas = list(map(float,stdin.readline().split()))

main()
