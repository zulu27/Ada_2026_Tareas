
<<<<<<< HEAD
S = "anitalabalatina"
memo = {}
print(len(S))
def backwards(i,j,c):
    if i >= j:
        ans = c
    
    elif S[i] == S[j]:
        ans = max(backwards(i+1,j-1,c+1),backwards(i,j-1,0),backwards(i+1,j,0))
    else:
        ans = max(backwards(i+1,j,0),backwards(i,j-1,0),c)
        
    return ans

def backwards_memo(i,j,c):
    key = (i,j,c)
    if i >= j:
        ans = c
    
    elif key in memo:
        ans = memo[key]
    
    elif S[i] == S[j]:
        ans = max(backwards_memo(i+1,j-1,c+1),backwards_memo(i,j-1,0),backwards_memo(i+1,j,0))
    else:
        ans = max(backwards_memo(i+1,j,0),backwards_memo(i,j-1,0),c)
    
    memo[key] = ans
    return ans

mem = [[-1 for _ in range(len(S))] for _ in range(len(S))]

def back(i,j):
    if mem[i][j] != -1:
        ans = mem[i][j]
    elif i >= j or S[i] != S[j]:
        ans = 0
    else:
        ans = 1 + back(i+1,j-1)
        mem[i][j] = ans 

    return ans

def recursion():
    maximo = -float('inf')
    for i in range(len(S)-2):
        j = len(S) - 1
        while j > 0:
            res = back(i,j)
            if res > maximo:
                maximo = res
            j -= 1
    return maximo
"""
def backwards_memo(i,j):
    key = (i,j)
    if i >= j:
        ans = 0
    
    elif key in memo:
        ans = memo[key]
    
    elif S[i] == S[j]:
        ans = max(backwards_memo(i+1,j-1) + 1,backwards_memo(i,j-1),backwards_memo(i+1,j))
        
    else:
        ans = max(backwards_memo(i+1,j),backwards_memo(i,j-1))
    
    memo[key] = ans
    return ans
"""
print(recursion())
#print(backwards_memo(0,len(S)-1,0))
=======
import copy
S = "REDIVIDE"
"""
def backwards(i,j):
    if i >= j:
        ans = 0
    else:
        if S[i] == S[j]:
            ans = backwards(i+1,j-1) + 1
        else:
            ans = max(backwards(i+1,j),backwards(i,j-1))
    
    return ans
"""

def backwards(i,j,c):

    if i >= j:
        ans = c
    else:
        if S[i] == S[j]:
            ans = backwards(i+1,j-1,c+1)
            ##ans = c + 1
            #print("Entre a la suma")
            #print(ans)
        else:
            ans = max(backwards(i+1,j,0),backwards(i,j-1,0),c)

    return ans
print(backwards(0,len(S) - 1,0))
>>>>>>> c8fa0a2d7e7e5e0390fd2838520afa3df3c8322b
