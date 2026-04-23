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

def revision(x,y,mom_c):
    ans = True
    for i in range(mom_c, 3):
        ans = (x,y) != (puntos_clave[i])
    return ans

def ice(x,y,vis,mom_c):
    global t
    global ans
    if (x,y) == (0,1) and vis == t:
        ans += 1
    
    elif (x,y) != (0,1):

        for i,j in movimientos:
            
            n_x = i + x
            n_y = j + y
            if n_x >= 0 and n_x < len(lago) and n_y >= 0 and n_y < len(lago[n_x]) and lago[n_x][n_y] == False:
                if mom_c < len(checks) and vis == checks[mom_c] and (x,y) == puntos_clave[mom_c]:

                    lago[n_x][n_y] = True
                    ice(n_x,n_y,vis+1,mom_c + 1)
                    lago[n_x][n_y] = False

                elif mom_c < len(checks) and vis < checks[mom_c] and revision(x,y,mom_c):

                    lago[n_x][n_y] = True
                    ice(n_x,n_y,vis + 1,mom_c)
                    lago[n_x][n_y] = False

                elif mom_c == 3:

                    lago[n_x][n_y] = True
                    ice(n_x,n_y,vis + 1,mom_c)
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