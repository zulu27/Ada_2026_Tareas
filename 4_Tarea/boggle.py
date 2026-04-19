"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
from heapq import heappop,heappush

heap = []
palabras = []
encontradas = set()
movement_matrix = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

class MiLista:
    def __init__(self, l):
        self.listica = l

    def __lt__(self, other):
        ans = False

        if len(self.listica) < len(other.listica):
            ans = True
        elif len(self.listica) == len(other.listica):
            ans = self.listica < other.listica

        return ans 

def boggle(tupla_sol,x,y):
    if len(tupla_sol.listica) >= 3:
        pal = ''.join(tupla_sol.listica)
        if pal not in encontradas:
            cop = MiLista(list(tupla_sol.listica))
            heappush(heap,cop)
            encontradas.add(pal)


    for i,j in movement_matrix:
        nuev_x = x+i
        nuev_y = y+j
        if nuev_x >= 0 and nuev_x < len(palabras) and nuev_y >= 0 and nuev_y < len(palabras[nuev_x]):
            if palabras[nuev_x][nuev_y] > tupla_sol.listica[-1]:
                tupla_sol.listica.append(palabras[nuev_x][nuev_y])
                boggle(tupla_sol,nuev_x,nuev_y)
                tupla_sol.listica.pop()


def main():
    cases = int(stdin.readline())



    for _ in range(cases):
        stdin.readline()
        cant_palabras = int(stdin.readline())
        for _ in range(cant_palabras):
            letras = list(stdin.readline().strip())
            palabras.append(letras)

        for i in range(len(palabras)):
            for j in range(len(palabras[i])):
                tupla_sol = MiLista([palabras[i][j]])
                boggle(tupla_sol,i,j)  

        if len(heap) != 0:
            while len(heap) > 0:
                l = heappop(heap)
                print(''.join(l.listica))
                
        heap.clear()
        palabras.clear()
        encontradas.clear()   
                
        


    return 0




main()