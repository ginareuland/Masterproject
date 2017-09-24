import numpy as np
from AllClosestPoints import AllClosestPoints
import itertools as it

def VoronoiRelevantVectors(H):

    N = []
    n = np.shape(H)[0]
    M = []
    M.append([])
    S= []
    S.append([])
    X=[]
    for p in it.product([0, 0.5], repeat=n):
        if p != tuple(np.zeros(n)):
           M[0].append(list(p))
    for s in M[0]:
        s = np.asarray(s)
        s = np.dot(s,H)
        S[0].append(list(s))
    for s in S[0]:
        X = AllClosestPoints(H,s)
        if len(X) == 2:
            for x in X:
                x= np.asarray(x)
                s = np.asarray(s)
                y= 2*x-2*s
                N.append(list(y))

    return N

#print(VoronoiRelevantVectors([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))
print(VoronoiRelevantVectors([[1,0,0,0],[0.5,1,0,0],[0,0,1,0],[1,1,1,1]]))
print(len(VoronoiRelevantVectors([[1,0,0,0],[0.5,1,0,0],[0,0,1,0],[1,1,1,1]])))
