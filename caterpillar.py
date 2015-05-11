'''def  countUneatenLeaves( N,  A):
    if N>10,000:
        max = 0
        parition = 1000
        countup = 10,000
        for i in range(1, )
'''

import math

def  countUneatenLeaves( N,  A):
    uneaten_leaves=0
    if len(A)==0:
        return N
    if 1 in A:
        return 0
    for leaf in range(1, N+1 ,1):
        check=False
        for caterpillar in A:
            if caterpillar != 0:
                if leaf%caterpillar == 0:
                    check=True
        if check==False:
            uneaten_leaves+=1
    return uneaten_leaves

res = countUneatenLeaves(math.pow(10,9), [2,4,5])
print res
