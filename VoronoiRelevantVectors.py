import numpy as np
from AllClosestPoints import AllClosestPoints
import itertools as it
import pprint

def VoronoiRelevantVectors(H):

    N = []
    n = np.shape(H)[0]
    M = []
    M.append([])
    S= []
    S.append([])
    X=[]
    for p in it.product([0, 0.5], repeat=n):    # Konstruiere alle möglichen Vektoren in [0,0.5]^n
        if p != tuple(np.zeros(n)):
           M[0].append(list(p))
    for s in M[0]:                              # Konstruire alle 2^n-1 vektoren in L/2L \ {0}
        s = np.asarray(s)
        s = np.dot(s,H)
        S[0].append(list(s))
    for s in S[0]:
        X = AllClosestPoints(H,s)
        if len(X) == 2:                      # wenn s Voronoi relevant, dann sind genau 2 LatticeVekotren s am nächsten
            for x in X:
                x= np.asarray(x)
                s = np.asarray(s)
                y= np.around(2*x-2*s)
                N.append(list(y))

    return N
# !! Basisvektoren sind die Reihenvektoren

if __name__ == '__main__':
  H= [[20,0,0,0],[-7,6,0,0],[10,5,2,0],[0,-4,-2,-30]]
  print((VoronoiRelevantVectors(H)))
  #print(np.dot(np.linalg.inv(np.matrix(H)),np.matrix(H)))
  print(len(VoronoiRelevantVectors(H)))
