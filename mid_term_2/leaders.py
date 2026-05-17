"""
Nombre: Cesar A Zuluaga
Codigo: 8989815
Fecha: 02/05/2026
"""

from sys import stdin
temas = []
prohibidos = {}
res = []

def no_conflict(tema,sol):
    i = 0
    flag = True
    while i < len(sol) and flag and tema in prohibidos:
        if sol[i] in prohibidos[tema]:
            flag = False
        
        i += 1
    return flag

def leaders(sol,s,n):
    global temas
    global prohibidos
    global res
    
    if s == 0:
        
        copia = list(sol)
        
        res.append(copia)
    
    elif len(temas) - n >= s:
        
        for i in range(n,len(temas)):
            if no_conflict(temas[i],sol):
                sol.append(temas[i])
                leaders(sol,s-1,i+1)
                sol.pop()


def main():
    cases = int(stdin.readline())
    global temas
    global prohibidos
    global res

    for i in range(cases):
        num_topicos,parejas_prohibidas, s_cantidad_topicos = map(int,stdin.readline().split())
        for _ in range(num_topicos):
            tema = stdin.readline()
            tema = tema.strip().upper()
            temas.append(tema)
        
        for _ in range(parejas_prohibidas):
            tem1,tem2 = stdin.readline().split()
            tem1 = tem1.strip().upper()
            tem2 = tem2.strip().upper()

            if tem1 not in prohibidos:
                prohibidos[tem1] = set()
            
            if tem2 not in prohibidos:
                prohibidos[tem2] = set()

            prohibidos[tem1].add(tem2)
            prohibidos[tem2].add(tem1)

        temas.sort(key = lambda x: (-len(x),x.lower()))
        t = 0
        while t < len(temas):
            leaders([temas[t]],s_cantidad_topicos-1,t+1)
            t += 1
        #res.sort(key=lambda grupo: [(-len(t), t.lower()) for t in grupo])

        print(f'Set {i+1}:')
        for tem in res:
            print(" ".join(tem))
        print()
        temas.clear()
        prohibidos.clear()
        res.clear()
main()