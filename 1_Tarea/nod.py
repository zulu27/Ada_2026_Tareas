###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto C
# Fecha 31/01/2026
#


from sys import stdin

divisores = [0] * 1000001
secuencia = [1]


def llenar_divisores():

    for i in range(1,1000001):
        j = i

        while j < 1000001:


            divisores[j] += 1
            j += i

llenar_divisores()



def nod(n):
    return divisores[n]

def ecua(n):
    res = secuencia[-1]

    if secuencia[-1] < n:
        while res < n:
            res = res + nod(res)
            secuencia.append(res)


def busqueda_a(n):
    bottom = 0
    top = len(secuencia)

    while  bottom < top:

        busq = (top + bottom) // 2

        if secuencia[busq] < n:
            bottom = busq + 1


        else:
            top = busq

    return bottom

def busqueda_b(n):
    bottom = 0
    top = len(secuencia)

    while bottom < top:

        busq = (top + bottom ) // 2

        if secuencia[busq] <= n:
            bottom = busq + 1


        else:
            top = busq

    return bottom



def main():
    n = int(stdin.readline())
    for i in range(n):
        a,b = map(int,stdin.readline().split())
        ecua(b)
        ans1 = busqueda_a(a)
        ans2 = busqueda_b(b)
        print(f'Case {i + 1}: {(ans2 - ans1)}')



main()