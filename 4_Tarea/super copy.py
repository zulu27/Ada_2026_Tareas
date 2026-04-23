"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin
num = [0,1,2,3,4,5,6,7,8,9]
ans = -1
flag = False

def super(m, i, sol, rem):
    global flag, ans

    if flag:
        return

    if i > m:
        ans = sol
        flag = True
        return

    for d in range(10):
        nuevo_rem = (rem * 10 + d) % i
        if nuevo_rem == 0:
            super(m, i+1, sol*10 + d, nuevo_rem)


def main():
    cases = int(stdin.readline())
    global ans
    global flag
    for i in range(cases):
        n,m = map(int,stdin.readline().split())
        flag = False
        inc = False
        count = 10**(n-1)
        maximo = 10**n

        
        while count < maximo and not flag:

            if count % n == 0:
                inc = True
                super(m, n+1, count, count % n)
            if inc:
                count += n
            else:
                count += 1

        print(f"Case {i+1}: {ans}")
        
        ans = -1
        flag = False

    return 0


main()