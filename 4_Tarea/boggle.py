"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
from heapq import heappop,heappush

res = []
palabras = []
encontradas = set()
movement_matrix = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]



def boggle(tupla_sol,x,y):
    if len(tupla_sol) >= 3:
        pal = ''.join(tupla_sol)
        if pal not in encontradas:
            res.append(pal)
            encontradas.add(pal)


    for i,j in movement_matrix:
        nuev_x = x+i
        nuev_y = y+j
        if nuev_x >= 0 and nuev_x < len(palabras) and nuev_y >= 0 and nuev_y < len(palabras[nuev_x]):
            if palabras[nuev_x][nuev_y] > tupla_sol[-1]:
                tupla_sol.append(palabras[nuev_x][nuev_y])
                boggle(tupla_sol,nuev_x,nuev_y)
                tupla_sol.pop()


def main():
    cases = int(stdin.readline())



    for n in range(cases):
        stdin.readline()
        cant_palabras = int(stdin.readline())
        for _ in range(cant_palabras):
            letras = list(stdin.readline().strip())
            palabras.append(letras)

        for i in range(len(palabras)):
            for j in range(len(palabras[i])):
                tupla_sol = [palabras[i][j]]
                boggle(tupla_sol,i,j)  

        res.sort(key=lambda s: (len(s), s))
        for i in res:
            print(i)
        
        if n != cases - 1:
            print()
        

        res.clear()
        palabras.clear()
        encontradas.clear()   
                
        


    return 0




main()