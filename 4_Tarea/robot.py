"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
lago = []
checks = []
puntos_clave = []
movimientos = [(1,0),(0,1),(-1,0),(0,-1)]
parejas_clave = {}
t = 0
ans = 0

def valido(x,y):
    return (x < len(lago) and x >= 0 and y < len(lago[x]) and y >=0) and not lago[x][y]



def aun_llego(mom_c,x,y,vis):
    res = True
    
    if mom_c == 3:
        dist = x + abs(y - 1)
        if vis + dist > t:
            res = False
    else:
        dist = abs(x- puntos_clave[mom_c][0]) + abs(y - puntos_clave[mom_c][1])
        #print(x,y,dist,puntos_clave[mom_c],vis,checks[mom_c])
        if vis + dist > checks[mom_c]:
            res = False

        if (x,y) == puntos_clave[mom_c] and vis < checks[mom_c]:
            res = False
        #print(res)
    
    return res

def revision5(x,y):
    Ux , Uy = x + 1, y
    Rx, Ry = x , y + 1
    Dx,Dy = x - 1, y
    Lx,Ly = x, y - 1
    res = True
    


    if not (valido(Ux,Uy) or valido(Dx,Dy)) and valido(Rx,Ry) and valido(Lx,Ly):
        res = False

    elif not (valido(Rx,Ry) or valido(Lx,Ly)) and  valido(Ux,Uy) and valido(Dx,Dy):
        res = False
    
    return res

def ice(x,y,vis,mom_c):
    global t
    global ans
    #print("vis ==",vis," ",x,y)
    if vis == t and (x,y) == (0,1):
        ans += 1
    
    else:
        for i,j in movimientos:
            n_x = x + i
            n_y = y + j

            if valido(n_x,n_y) and aun_llego(mom_c,n_x,n_y,vis + 1):
                #print("procese")
                lago[n_x][n_y] = True
                if revision5(n_x,n_y):
                    if mom_c < 3 and (n_x,n_y) == puntos_clave[mom_c]:
                        ice(n_x,n_y,vis + 1, mom_c + 1)
                    else:
                        ice(n_x,n_y,vis +1, mom_c)
                lago[n_x][n_y] = False
         

def main():
    n,m = map(int,stdin.readline().split())
    j = 1
    global t
    global ans
    while n != 0 and m != 0:

        for i in range(n):
            lago.append([])
            for _ in range(m):
                lago[i].append(False)

        puntos = list(map(int,stdin.readline().split()))
        puntos_clave.append((puntos[0],puntos[1]))
        puntos_clave.append((puntos[2],puntos[3]))
        puntos_clave.append((puntos[4],puntos[5]))
        
        ans = 0
        t = n*m
        checks.append(t//4)
        checks.append(t//2)
        checks.append((3*t)//4)

        #print(checks)
        
        lago[0][0] = True
        ice(0,0,1,0)

        print(f'Case {j}: {ans}')

        ans = 0
        j += 1
        lago.clear()
        checks.clear()
        puntos_clave.clear()
        n,m = map(int,stdin.readline().split())

    return 0

main()