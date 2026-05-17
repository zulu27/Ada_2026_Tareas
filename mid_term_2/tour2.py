"""
Nombre: Cesar A Zuluaga
Codigo: 8989815
Fecha: 02/05/2026
Para unir los conjuntos utilice lo que esta documentado en esta pagina:
https://www.w3schools.com/python/python_sets_join.asp
"""
#hacerlo con set y cada vez que jubte cosas reviso todas las aristas de lo que esta adentro

from sys import stdin

tamanos = []
orden_procesar = []
grafo,p, rango = [], [],[]
miembros = {}
INF = float('inf')

def makeSet(v):
    p[v], rango[v],tamanos[v] = v, 0,1
    miembros[v] = {v}

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
        miembros[u] |= miembros[v]




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
    
    i = 0
    while i < len(aristas):
        k,u,v = aristas[i][0],aristas[i][1],aristas[i][2]

        if findSet(u) != findSet(v):
            unionSet(u,v)
            raiz = findSet(u)
            externo = 0
            interno = INF
            for islas in miembros[raiz]:
                for a,k in grafo[islas]:
                    if a in miembros[raiz]:
                        interno = min(interno,k)
                    else:
                        externo = max(externo,k)
            
            if interno > externo:
                res += tamanos[raiz]
        i += 1
    return res


def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        n,m = map(int,stdin.readline().split())

        for _ in range(n):
            tamanos.append(0)
            p.append(0)
            rango.append(0)
            grafo.append([])
        
        for _ in range(m):
            u,v,k = map(int,stdin.readline().split())
            u = u-1
            v = v-1
            a = max(u,v)
            b = min(u,v)
            orden_procesar.append((k,a,b))

            grafo[u].append((v,k))
            grafo[v].append((u,k))

        orden_procesar.sort(key=lambda x: -x[0])

        ans =  kruskal(orden_procesar,n)
        print(ans)
        tamanos.clear()
        orden_procesar.clear()
        p.clear()
        rango.clear()
        grafo.clear()

main()