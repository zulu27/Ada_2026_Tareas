"""
Nombre: César Zuluaga
Codigo: 8989815
36 30 000000100111111110010000111110

"""

from sys import stdin
transformaciones = {}
candidatos = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
estado = None
flag = False
num_cell = 0

def crear_transformaciones(identificador):
    for i in range(8):
        trans = identificador & 1
        transformaciones[i] = trans
        identificador = identificador >> 1

def check(sol,num_cell):
    ans = False
    pos = len(sol) - 2
    izq = sol[pos - 1] << 2
    mit = sol[pos] << 1
    der = sol[pos + 1]

    trans = izq | mit | der
    trans = transformaciones[trans]
    corrimiento = num_cell - (len(sol) - 1)
    revi = (estado >> corrimiento) & 1

    if revi == trans:
        ans = True

    return ans


def revision_final(sol,num_cell):
    ans1 = check(sol,num_cell)
    ans2 = False

    izq = sol[len(sol) - 2] << 2
    mit = sol[len(sol) - 1] << 1
    der = sol[0]

    trans = izq | mit | der
    trans = transformaciones[trans]
    revi = estado & 1

    if revi == trans:
        izq = sol[len(sol) - 1] << 2
        mit = sol[0] << 1
        der =  sol[1]

        trans = izq | mit | der
        trans = transformaciones[trans]
        revi = estado >> (num_cell - 1)
        revi = revi & 1

        if revi == trans:
            ans2 = True


    return ans1 & ans2

def eden(sol):
    global flag
    global num_cell
    #print("itere")
    if len(sol) == num_cell:
        flag = revision_final(sol,num_cell)


    elif check(sol,num_cell) and not flag:
        sol.append(0)
        eden(sol)
        if not flag:
            sol[-1] = 1
            eden(sol)
        sol.pop()
        


def main():
    line = stdin.readline()
    global estado
    global flag
    global num_cell

    while line != "":
        identificador, num_cell, estado = map(int,line.split())
        crear_transformaciones(identificador)
        flag = False
        #print(transformaciones)
        i = 0
        estado = int(str(estado),2)
        #print(i< len(candidatos) and not flag)
        while i < 8 and not flag:
            #print("aja")
            eden(candidatos[i])
            i += 1

        if flag:
            print("REACHABLE")
        
        else:
            print("GARDEN OF EDEN")

        line = stdin.readline()


main()