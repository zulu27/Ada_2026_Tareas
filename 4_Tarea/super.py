"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
num = [0,1,2,3,4,5,6,7,8,9]
ans = -1

def super(m,i,sol):
    global ans
    
    if ans == 1020005460:
        print("Lo ecnontre")
    if i > m:
        if ans == -1 or ans > sol:
            ans = int(sol)

    else:

        sol= 10*sol
        for numero in num:
            sol += numero
            if sol % i == 0:
                
                super(m,i+1,sol)
            sol-= numero
                
        sol = sol//10


def main():
    cases = int(stdin.readline())
    global ans
    for _ in range(cases):
        n,m = map(int,stdin.readline().split())

        
        count = 10**(n-1)
        maximo = 10**n


        while count < maximo:

            if count % n == 0:

                super(m,n+1,count)
            count += 1

        print(ans)
        
        ans = -1


    return 0


main()