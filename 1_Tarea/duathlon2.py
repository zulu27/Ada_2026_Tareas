###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto B
# Fecha 31/01/2026
#
#la busqueda ternaria utilizada en este ejercicio fue basada y construida gracias a la ayuda del siguiente texto
# https://cp-algorithms.com/num_methods/ternary_search.html
from sys import stdin

participantes = []


def tiempo(r, t):
    mejor = float('inf')
    k = t - r

    for c in range(len(participantes) - 1):
        tiempo_r = r / participantes[c][0]
        tiempo_k = k / participantes[c][1]

        if mejor >= (tiempo_r + tiempo_k):
            mejor = tiempo_r + tiempo_k

    tiempo_r = r / participantes[-1][0]
    tiempo_k = k / participantes[-1][1]

    ans = mejor - (tiempo_r + tiempo_k)

    return ans

def duathlon(t,right,left):


    if right - left > 0.00001:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3

        if tiempo(m1,t) < tiempo(m2,t):
            left = m1
            left = duathlon(t,right,left)
        else:
            right = m2
            left = duathlon(t,right,left)


    return left


def main():
    line = stdin.readline()

    while line != "":
        if line != "\n":
            t = int(line)
            n = int(stdin.readline())
            for _ in range(n):
                (r, c) = map(float, stdin.readline().split())

                participantes.append([r, c])

            r = duathlon(t,t,0)
            k = t - r

            tmp = tiempo(r, t)

            if tmp > 0:

                tmp = tmp * 3600
                tmp = round(tmp,2   )
                tmp = int(tmp)


                print(f"The cheater can win by {tmp} seconds with r = {r:.2f}km and k = {k:.2f}km.")

            else:
                print("The cheater cannot win.")
        participantes.clear()
        line = stdin.readline()


main()