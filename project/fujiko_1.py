"""
Nombre: César A. Zuluaga
Codigo: 8989815
Fecha:
"""

from sys import stdin

arbol = [[] for _ in range(501)]
hijos_transmi = [0 for _ in range(501)]
nodos_transmi = {}
padres = set()
hijos = set()
tabu = []

NEG_INF = -float('inf')

def calc_hijos_transmi(x):
    ans = 0
    if x in nodos_transmi:
        ans += 1
    
    for hijo,_ in arbol[x]:
        ans += calc_hijos_transmi(hijo)
    
    hijos_transmi[x] = ans
    return ans

def crear_tabu(n,k):
    global tabu,arbol,nodos_transmi,hijos_transmi
    for nodo in range(n):
        tabu.append([])
        for infect in range(k+1):
            tabu[nodo].append([])
            tabu[nodo][infect].append(NEG_INF)
            tabu[nodo][infect].append(NEG_INF)
            if len(arbol[nodo]) == 0 or infect == 0:
                tabu[nodo][infect][0] = 0
                tabu[nodo][infect][1] = 0


def f(hijo,pres):
    ans = 0
    if hijos_transmi[hijo] >= pres:
        ans = phi(hijo,pres,0)
    return ans

def g(x,pres):
    global tabu,arbol,nodos_transmi,hijos_transmi
    ans = 0

    if len(arbol[x]) == 1 and pres > 0 and hijos_transmi[arbol[x][0][0]] >= pres:
        ans = arbol[x][0][1] + phi(arbol[x][0][0],pres,1)
    
    elif len(arbol[x]) == 2 and pres > 0:
        hijo1 = arbol[x][0][0]
        hijo2 = arbol[x][1][0]

        i = 0
        while i <= hijos_transmi[hijo1] and i <= pres:
            j = pres - i
            if j <= hijos_transmi[hijo2]:
                ans = max(ans, ganancia(x,0,i,j,0) + ganancia(x,1,j,i,0))
                
            i += 1

    elif len(arbol[x])  == 3 and pres > 0:
        hijo1 = arbol[x][0][0]
        hijo2 = arbol[x][1][0]
        hijo3 = arbol[x][2][0]
        i = 0
        while i <= hijos_transmi[hijo1] and i <= pres:
            j = 0
            while j <= hijos_transmi[hijo2] and i+j <= pres:
                z = pres - i - j
                if z <= hijos_transmi[hijo3]:
                    ans = max(ans, ganancia(x,0,i,j,z) + ganancia(x,1,j,i,z) + ganancia(x,2,z,i,j))
                j += 1
            i += 1

    return ans

def ganancia(x,v,i,j,z):
    global tabu,arbol,nodos_transmi,hijos_transmi
    ans = 0
    if i != 0 :
        ans = arbol[x][v][1] + phi(arbol[x][v][0],i,1)
    return ans

def phi(x,pres,e):
    global tabu,arbol,nodos_transmi,hijos_transmi
    
    ans = 0
    if tabu[x][pres][e] != NEG_INF:
        ans = tabu[x][pres][e]

    elif pres == 0 or len(arbol[x]) == 0:
        ans = 0
    
    else:
        if x not in nodos_transmi:
            if e == 0:
                for hijo, _ in arbol[x]:
                    ans = max(ans,f(hijo,pres))

            else:
                ans = g(x,pres)

        else:
            if e == 1:
                ans = g(x,pres-1)

            else:
                for hijo, _ in arbol[x]:
                    ans = max(ans,f(hijo,pres))
                
                ans = max(ans,g(x,pres-1))
        
    
    tabu[x][pres][e] = ans

    return ans

def main():
    global tabu,arbol,nodos_transmi,hijos_transmi
    line = stdin.readline()

    while line != "":
        nodos,transmi,q = map(int,line.split())

        for _ in range(nodos-1):
            padre, hijo, costo = map(int,stdin.readline().split())
            if padre not in hijos:
                padres.add(padre)

            if hijo in padres:
                padres.remove(hijo)

            arbol[padre].append((hijo,costo))

        padre_arbol = padres.pop()

        nodos_transmi = set(map(int,stdin.readline().split()))
        querys = list(map(int,stdin.readline().split()))

        calc_hijos_transmi(padre_arbol)
        crear_tabu(nodos,querys[-1])
        

        for presupuesto in querys:
            print(phi(padre_arbol,presupuesto,0))

        

        for i in range(nodos):
            arbol[i].clear()
            hijos_transmi[i] = 0
        tabu.clear()
        padres.clear()
        hijos.clear()
        line = stdin.readline()
main()