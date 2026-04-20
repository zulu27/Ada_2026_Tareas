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

ans = 0

def ice(vis,x,y,check,t,puntos_clave):
    global ans
    pareja = parejas_clave[check]
    #print(vis)
    if vis == t and x == 0 and y == 1 and check == 3:
        print("hola")
        ans += 1
    
    elif check < 3:
        clave_x = puntos_clave[pareja[0]]
        clave_y = puntos_clave[pareja[1]]

        if checks[check] == vis and x == clave_x and y == clave_y:
            lago[x][y] = True
            for nx,ny in movimientos:
                i = x + nx
                j = y + ny
                if i >= 0 and i < len(lago) and j >= 0 and j < len(lago[i]) and lago[i][j] == False:
                    ice(vis + 1,i,j,check + 1,t,puntos_clave)
            lago[x][y] = False

        elif checks[check] > vis and (x,y) != (clave_x,clave_y):
            
            lago[x][y] = True
            for nx,ny in movimientos:
                i = x + nx
                j = y + ny
                if i >= 0 and i < len(lago) and j >= 0 and j < len(lago[i]) and lago[i][j] == False:
                    ice(vis + 1,i,j,check,t,puntos_clave)
            lago[x][y] = False

def main():
    n,m = map(int,stdin.readline().split())
    i = 1
    parejas_clave[0] = (0,1)
    parejas_clave[1] = (2,3)
    parejas_clave[2] = (4,5)
    
 
    while n != 0 and m != 0:
        for i in range(n):
            lago.append([])
            for _ in range(m):
                lago[i].append(False)

        puntos_clave = list(map(int,stdin.readline().split()))

        t = n*m
        checks.append(t//4)
        checks.append(t//2)
        checks.append((3*t)//4)

        #print(checks)
        
        lago[0][0] = True
        ice(1,0,0,0,t,puntos_clave)

        print(ans)
        ans = 0
        i += 1
        lago.clear()

        n,m = int(stdin.readline().split())

    return 0

main()