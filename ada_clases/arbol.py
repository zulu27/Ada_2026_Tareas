"""
Implementacion arboles binarios 
:) en clase
"""

from collections import deque
from heapq import heappush, heappop
f = {}

class BinTree(object):
    """A binary tree that is either a leaf or a label with exactly 2 subtrees"""

    def __init__(self,label,left = None, right=None):
        #Creates a binary tree with a label and two children
        self.__label = label
        self.__left = left
        self.__right = right
    
    def isLeaf(self):
        return self.__left == None and self.__right == None
    
    def getLabel(self):
        return self.__label
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def traverse(self):
        s = list()
        self.__traverseAux(s)
    
    def __traverseAux(self,pref):
        if self.isLeaf(): print(''.join(pref) + ' : ' + self.__label)
        else:
            pref.append('0')
            self.getLeft().__traverseAux(pref)
            pref.pop()
            pref.append('1')
            self.getRight().__traverseAux(pref)
            pref.pop()
    

def solve(f):
    forest = list()

    for k in f:
        heappush(forest,(f[k],BinTree(k)))
    
    
    for i in forest:
        print(i)


    while len(forest) > 1:
        v1,left = heappop(forest)
        v2,right = heappop(forest)

        heappush(forest,((v1+v2),BinTree(left.getLabel()+ right.getLabel(),left,right)))

    print(forest)
    return heappop(forest)
        
    
freq  = dict()
freq['a'] = 45
freq['b'] = 13
freq['c'] = 12
freq['d'] = 16
freq['e'] = 9
freq['f'] = 5

_, code = solve(freq)
print(code)
code.traverse()