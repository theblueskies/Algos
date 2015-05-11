import math

def getNumberOfPrimes( N):
    total=0
    if N == 2:
        return 1
    for x in range(3, N, 2):
        check = check_prime(x)
        if check:
            total+=1
    return total



def check_prime(num):
    if num==2 or num==3 or num==5 or num==7:
        return True
    check = False
    loop_max = int(math.sqrt(num))
    for x in range(3,loop_max,1):
        if num%x == 0:
            check = False
            return check
        else:
            check = True
    return check

res = getNumberOfPrimes(100)
print res
