#Nombre: César A. Zuluaga
#Codigo: 8989815
#Fecha: 28/02/2026

from sys import stdin

city = [[0 for _ in range(1010)] for _ in range(1010)]
querys = []
ranges = {}
coffes = []


def coffe(dx,dy,m):

    for x,y in coffes:

        for fila in range(max(1, y - m), min(dy, y + m) + 1):
            ancho = m - abs(fila - y)
            left = max(1, x - ancho)
            right = min(dx, x + ancho)

            if fila not in ranges:
                ranges[fila] = []

            ranges[fila].append((left,1))
            ranges[fila].append((right , -1))

    caffe_historico = 0
    current_best_x = float('inf')
    current_best_y = float('inf')

    for y in sorted(ranges):
        ranges[y].sort(key=lambda e: (e[0], -e[1]))

        caffe_it = 0
        caffe_h_it = 0
        current_x = float('inf')
        for x, val in ranges[y]:
            
            caffe_it += val 

            if caffe_it > caffe_h_it:
                current_x = x
                caffe_h_it = caffe_it

            elif caffe_h_it == caffe_it:
                current_x = min(current_x, x)


        if caffe_historico < caffe_h_it:
            caffe_historico = caffe_h_it
            current_best_x = current_x
            current_best_y = y
        
        elif caffe_h_it == caffe_historico:
            if y < current_best_y:
                current_best_x = current_x
                current_best_y = y

            elif current_x < current_best_x and y == current_best_y:
                current_best_x = current_x

    return [caffe_historico,current_best_x,current_best_y]


def main():
    dx, dy, n , q = map(int,stdin.readline().split())
    i = 1
    while (dx + dy + n + q) != 0:
        for _ in range(n):
            x,y = map(int,stdin.readline().split())
            coffes.append((x,y))

        for _ in range(q):
            v = int(stdin.readline())
            querys.append(v)

        print(f'Case {i}:')
        i += 1
        for m in querys:
            ans = coffe(dx,dy,m)
            ranges.clear()
            print(f'{ans[0]} ({ans[1]},{ans[2]})')

        querys.clear()
        coffes.clear()
        dx, dy, n , q = map(int,stdin.readline().split())

main()