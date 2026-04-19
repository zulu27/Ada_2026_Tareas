"""
Nombre: César Zuluaga
Codigo: 8989815
Date: 25/03/2026
"""

from sys import stdin
from collections import deque

def calculus(N,E):
    ans = 0
    menor = 0
    mayor = len(N) - 1
    n = 0
    pros = 0
    pila = deque()
    #True es que inverti el estado
    #False es que no inverti el estado

    while pros <= len(N) - 1:
        if n == 0 and E[n] == 'x':
                ans = N[mayor]
                mayor -= 1
                pros += 1

        elif n == 0 and E[n] == '(':
            pila.append(0)

        elif len(pila) == 0 or pila[-1] == False:
            
            if E[n] == 'x' and E[n - 1] == '+':
                ans += N[mayor]
                mayor -= 1
                pros += 1
                
            elif E[n] == 'x' and E[n-1] == '-':
                ans -= N[menor]
                menor += 1
                pros += 1
                
            elif E[n] == 'x' and E[n-1] == '(':
                ans += N[mayor]
                mayor -= 1
                pros += 1
                
            elif E[n] == '(' and E[n - 1] == '-':
                if len(pila) != 0:
                    pila.append(not pila[-1])
                else:
                    pila.append(True)

                
            elif E[n] == '(' and E[n - 1] == '+':

                if len(pila) != 0:
                    pila.append(pila[-1])
                else:
                    pila.append(False)

            elif E[n] == '(' and E[n - 1] == '(':
                pila.append(pila[-1])

            elif E[n] == ')':
                pila.pop()

        else:
                if E[n] == 'x' and E[n - 1] == '+':
                    ans -= N[menor]
                    menor += 1
                    pros += 1
                
                elif E[n] == 'x' and E[n-1] == '-':
                    ans += N[mayor]
                    mayor -= 1
                    pros += 1
                
                elif E[n] == 'x' and E[n-1] == '(':
                    ans -= N[menor]
                    menor += 1
                    pros += 1
                
                elif E[n] == '(' and E[n - 1] == '-':
                    if len(pila) != 0:
                        pila.append(not pila[-1])
                    else:
                        pila.append(False)

                elif E[n] == '(' and E[n - 1] == '+':
                    if len(pila) != 0:
                        pila.append(pila[-1])
                    else:
                        pila.append(True)

                
                elif E[n] == '(' and E[n - 1] == '(':
                    pila.append(pila[-1])
            
                elif E[n] == ')':
                        pila.pop()
        n += 1

    return ans    
def main():
    cases = int(stdin.readline())
    ecuacion = ""
    for _ in range(cases):
        ecuacion = stdin.readline()
        nums = int(stdin.readline())
        numeros = list(map(int,stdin.readline().split()))
        numeros.sort()
        ans = calculus(numeros,ecuacion)
        print(ans)



main()