import numpy as np


def myround(x):
    if np.ceil(x) - x <= x - np.floor(x):
        return np.ceil(x)
    else:
        return np.floor(x)

def sgn(y):
    if y <= 0:
        return -1
    else:
        return 1


def AllClosestPoints(H, x):


    H = np.matrix(H)
    H = H.getI()
    n = np.shape(H)[0]
    H = np.full((n, n), H, np.float)
    bestdist = float('inf')
    k = n
    dist = np.zeros(n, dtype=np.float)
    e = np.full((n, n), 0, np.float)
    e[k - 1] = np.dot(x, H)
    u = np.zeros(n)
    u[k - 1] = myround(e[k - 1][k - 1])
    y = (e[k - 1][k - 1] - u[k - 1]) / H[k - 1][k - 1]
    step = np.zeros(n)
    step[k - 1] = sgn(y)
    a=0.2
    U = []
    U.append([])

    while True:
        newdist = dist[k - 1] + y * y
        if newdist < (1+a)*bestdist:
            if k - 1 != 0:
                for i in range(0, k - 1):
                    e[k - 2][i] = e[k - 1][i] - y * H[k - 1][i]
                k = k - 1
                dist[k - 1] = newdist
                u[k - 1] = myround(e[k - 1][k - 1])
                y = (e[k - 1][k - 1] - u[k - 1]) / H[k - 1][k - 1]
                step[k - 1] = sgn(y)
            else:
                # if y == 0:         ## Teil braucht man für richtiges funktionieren von AllClosestPoints
                #    c = list(u)     ## für den Fall wo target vector ein integer vector ist
                #    U[0].append(c)  ## aber Teil unötig für
                #  else:
                if newdist !=0:
                       c = list(u)
                       U[0].append(c)
                       bestdist = min(bestdist,newdist)
                u[k - 1] = u[k - 1] + step[k - 1]
                y = (e[k - 1][k - 1] - u[k - 1]) / H[k - 1][k - 1]
                step[k - 1] = -step[k - 1] - sgn(step[k - 1])
        else:
            if k == n:
                i=0
                m= np.zeros(len(U[0]))
                for v in U[0]:
                    m[i] = np.linalg.norm(np.dot(v,np.linalg.inv(H))-x)
                    i=i+1
                minimum = min(list(m))
                X=[]
                X.append([])
                for v in U[0]:
                    if np.linalg.norm(np.dot(v,np.linalg.inv(H))-x) == minimum:
                        X[0].append(list(np.dot(v,np.linalg.inv(H))))
                return X[0]
            else:
                k = k + 1
                u[k - 1] = u[k - 1] + step[k - 1]
                y = (e[k - 1][k - 1] - u[k - 1]) / H[k - 1][k - 1]
                step[k - 1] = -step[k - 1] - sgn(step[k - 1])

print(AllClosestPoints([[1,0],[0,1]],[1,3]))


