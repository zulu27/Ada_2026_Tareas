"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""
from sys import stdin
from heapq import heappop,heappush

INF = float('inf')


class Estados:
    def __init__(self,piso,ascensor,costo):
        self.piso = piso
        self.ascensor = ascensor
        self.costo = costo

    def getPiso(self):
        return self.piso
    
    def getAscensor(self):
        return self.ascensor
    
    def getCosto(self):
        return self.costo


    def __lt__(self, other):
        return self.costo < other.costo

def dijkstra(k,demora,ascensor,max_ascensores,piso):
    queue = []
    procesados = {}
    llegue = False
    for asc in piso[0]:
        dem = demora[asc]*max_ascensores[asc]
        heappush(queue,Estados(0,asc,dem))

    while len(queue) != 0 and not llegue :
        act = heappop(queue)
        ans = INF
        if act.getPiso() == k:
            llegue = True
            ans = act.getCosto()
        #si ya procesamos ignoramos
        elif (act.getPiso(),act.getAscensor()) not in procesados:
            for asc in piso[act.getPiso()]:
                
                if asc != act.getAscensor():
                    mas_l = max(abs(max_ascensores[asc] - act.getPiso()), act.getPiso()) * demora[asc]
                    Estado_nuevo = Estados(act.getPiso(),asc,act.getCosto()+5 + mas_l)
                    heappush(queue,Estado_nuevo)

            for parada in ascensor[act.getAscensor()]:
                if parada != act.getPiso():
                    mas_l = abs(act.getPiso() - parada)*demora[act.getAscensor()]
                    Estado_nuevo = Estados(parada,act.getAscensor(),act.getCosto() + mas_l)
                    heappush(queue,Estado_nuevo)

        procesados[(act.getPiso(),act.getAscensor())] = act.getCosto()

    return ans

def main():
    line = stdin.readline()

    while line != "":
        demora = []
        ascensor = [] #todas las paradas de un ascensor 
        max_ascensores = [] #el piso más alto al que llega un ascensor
        piso = {} #que ascensores paran en un piso
        

        elevators, dest = map(int,line.split())
        demora = list(map(int, stdin.readline().split()))

        i = 0
        while i < elevators:
            paradas = list(map(int, stdin.readline().split()))
            ascensor.append(paradas)
            max_ascensores.append(paradas[-1])
            for j in paradas:
                if j not in piso:
                    piso[j] = []

                piso[j].append(i)


            i += 1
        
        if dest == 0:
            print(0)

        elif dest in piso:
            ans = dijkstra(dest,demora,ascensor,max_ascensores,piso)
            if ans != INF:
                print(ans)
            else:
                print("IMPOSIBLE")    

        else:
            print("IMPOSIBLE")

        line = stdin.readline()

        demora.clear()
        ascensor.clear()
        max_ascensores.clear()
        piso.clear()


main()