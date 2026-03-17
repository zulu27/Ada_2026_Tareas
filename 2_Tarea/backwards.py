
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