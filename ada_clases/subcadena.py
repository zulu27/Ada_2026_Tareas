from sys import stdin

def subcadenas(i, sol, S, D):
    ans = None
    if i == len(S):
        ans = list(sol)
        ans.pop()
    else:
        k, ans = i + 1, []
        while k <= len(S) and len(ans) == 0:
            word = S[i:k]
            if word in D:
                sol.append(k)
                ans = subcadenas(k, sol, S, D)
                sol.pop()
            k += 1
    return ans
