###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto B
# Fecha 31/01/2026
#
from sys import stdin
participantes = []


def tiempo(r,t):
    mejor = 1000000
    k = t - r

    for c in range(len(participantes) - 1):
        tiempo_r = r/participantes[c][0]
        tiempo_k = k/participantes[c][1]

        if mejor > (tiempo_r + tiempo_k):
            mejor = tiempo_r + tiempo_k

    tiempo_r = r/participantes[-1][0]
    tiempo_k = k/participantes[-1][1]

    ans = (tiempo_r + tiempo_k) - mejor

    return ans


def duatlhon(t):
    bottom = 0
    top = t
    calc_r = tiempo(t, t)
    calc_k = tiempo(0, t)
    

    while (top - bottom) > 0.0000001:
        mit = ((top + bottom) / 2)
        calc = tiempo(mit,t)
        #print(int(round(,0)))
        
        if calc_r <= calc_k:
            if calc <= calc_k:
                calc_k = calc
                bottom = mit

        else:
            if calc <= calc_r:
                top = mit
                calc_r = calc


    return mit






def main():

    line = stdin.readline()


    while line != "":
        if line != "\n":
            t = int(line)
            n = int(stdin.readline())
            for _ in range(n):
                (r,c) = map(float,stdin.readline().split())

                participantes.append([r,c])

            r = duatlhon(t)
            k = t - r
            
            tmp = tiempo(r,t)



            if tmp < 0:
                tmp = tmp*-1
                tmp = tmp * 3600
                tmp = int(round(tmp, 0))

                print(f"The cheater can win by {tmp} seconds with r = {r:.2f}km and k = {k:.2f}km.")

            else:
                print("The cheater cannot win.")
        participantes.clear()
        line = stdin.readline()






main()