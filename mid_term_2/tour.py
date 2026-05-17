"""
Nombre: Cesar A Zuluaga
Codigo: 8989815
Fecha: 02/05/2026
"""

from sys import stdin

tamanos = []
orden_procesar = []
p, rango = [], []

def makeSet(v):
    p[v], rango[v],tamanos[v] = v, 0,1

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)

    if u != v:
        tam = tamanos[u] + tamanos[v]
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1
        tamanos[u] = tam
        tamanos[v] = 0




def kruskal(aristas,n):
    global total
    total = 0
    res = 0
    sume_tamano = False
    ult = aristas[0][0]
    cola = set()
    # Inicializar DSU
    for i in range(len(tamanos)):
        makeSet(i)

    # Ordenar aristas por peso (ascendente)
    

    # Recorrer aristas
    i = 0
    while i < len(aristas) and not sume_tamano:
        e = aristas[i]
        
        u = e[1]
        v = e[2]
        
        #print(cola)
        if ult > e[0]:
            #print("entre")
            for elem in cola:

                #print("lo que suma ",tamanos[cola[0]])
                res += tamanos[elem]
                if tamanos[elem] == n:
                    sume_tamano = True
                
                #print("lo que queda ",res)
            cola.clear()
            ult = e[0]

        if findSet(u) != findSet(v):
            if findSet(v) in cola:
                cola.remove(findSet(v))
            if findSet(u) in cola:
                cola.remove(findSet(u))

            unionSet(u, v)
            #print("esto " ,findSet(u))
            raiz = findSet(u)
            cola.add(raiz)
            
            #print(cola)
            
        i += 1
    if not sume_tamano:
        res += n
    return res




def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        n,m = map(int,stdin.readline().split())

        for _ in range(n):
            tamanos.append(0)
            p.append(0)
            rango.append(0)
        
        for _ in range(m):
            u,v,k = map(int,stdin.readline().split())
            u = u-1
            v = v-1
            a = max(u,v)
            b = min(u,v)
            orden_procesar.append((k,a,b))

            #grafo[u].append((v,k))
            #grafo[v].append((u,k))

        orden_procesar.sort(key=lambda x: -x[0])

        ans =  kruskal(orden_procesar,n)
        print(ans)
        tamanos.clear()
        orden_procesar.clear()
        p.clear()
        rango.clear()

main()