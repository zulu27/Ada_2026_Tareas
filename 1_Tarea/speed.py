###
# Nombre: César Zuluaga
# Codigo 8989815
# Punto E
# Fecha 31/01/2026
#

from sys import stdin

journey = []

def time(e):
    tiempo = 0

    for i in journey:
        tiempo += i[0]/(i[1] + e)

    return tiempo

def business(t,s,d):

    top = ((len(journey)*d)/t) - s + 1
    bottom = s*(-1)
    res = 0

    while abs(top - bottom) > 0.0000000001 and abs(res - t) > 0.0000001:
        mit = (top + bottom)/2
        res = time(mit)

        if res <= t:
            top = mit

        elif res > t:
            bottom = mit

    return mit


def main():
    line = stdin.readline()


    while line != "":
        smallest = 1001
        distance = 0
        biggest_distance = 0
        journey.clear()
        n , t = map(int, line.split())

        for _ in range(n):
            d,s = map(int, stdin.readline().split())
            journey.append([d,s])

            if s < smallest:
                smallest = s

            if d > biggest_distance:
                biggest_distance = d
            distance += d


        ans = business(t,smallest,biggest_distance)
        #round(ans,10)
        print(f'{ans:.9f}')
        line = stdin.readline()



main()