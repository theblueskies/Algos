def itefun():
    arr = [3,7,1,11,5]
    i=0
    j=len(arr)-1
    while i<=j:
        i+=1
        if i==j:
            return arr[i]
        j-=1
    return arr[j]

res=itefun()
print res
