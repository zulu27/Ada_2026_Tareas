"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
num = [0,1,2,3,4,5,6,7,8,9]
ans = -1
flag = False

def super(m,i,sol):
    global ans
    global flag

    if i > m:
        flag = True
        ans = int(sol)

    else:
        
        sol= 10*sol
        j = 0
        while j < len(num) and not flag:
            numero = num[j]
            sol += numero
            if sol % i == 0:
                super(m,i+1,sol)
            sol-= numero
            j += 1
        """
        for numero in num:
            sol += numero
            if sol % i == 0:
                
                super(m,i+1,sol)
            sol-= numero
        """        
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
        flag = False

    return 0


main()