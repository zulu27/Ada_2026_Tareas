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

def ice(x,y,vis,mom_c):
    if x == 0 and y == 1:
        ans += 1
    
    else:

        
            
        for i,j in movimientos:
            n_x = i + x
            n_y = j + y
            if n_x >= 0 and n_x < len(lago) and n_y >= 0 and n_y < len(lago[n_x]) and lago[n_x][n_y] == False:
                if mom_c < len(checks) and vis == checks[mom_c] and (x,y) == puntos_clave[mom_c]:
                    lago[n_x][n_y] = True
                    ice(x,y,vis+1,mom_c + 1)
                    lago[n_x][n_y] = False

                elif vis < checks[mom_c] and (x,y) not in 
                    
         

def main():
    n,m = map(int,stdin.readline().split())
    i = 1
 
    while n != 0 and m != 0:

        for i in range(n):
            lago.append([])
            for _ in range(m):
                lago[i].append(False)

        puntos = list(map(int,stdin.readline().split()))
        puntos_clave.append((puntos[0],puntos[1]))
        puntos_clave.append((puntos[2],puntos[3]))
        puntos_clave.append((puntos[4],puntos[5]))
        
        
        t = n*m
        checks.append(t//4)
        checks.append(t//2)
        checks.append((3*t)//4)

        #print(checks)
        
        lago[0][0] = True
        ice(0,0,1,0)

        print(ans)
        ans = 0
        i += 1
        lago.clear()

        n,m = int(stdin.readline().split())

    return 0

main()