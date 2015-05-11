__author__ = 'blade'

def pivot(arr, low, high):
    if high<low:
        return -1
    if high==low:
        return low
    mid = (low+high)//2
    if mid<high and arr[mid]>arr[mid+1]:
        return mid,
    if mid>low and arr[mid]<arr[mid-1]:
        return (mid-1),
    if arr[low]>=arr[mid]:
        return pivot(arr, low, mid-1),
    else:
        return pivot(arr, mid, high),

def caller():
    l = [3,4,5,6,1,2]
    pos = pivot(l,0,len(l)-1)
    print "Index of where it is pivoted is", pos[0][0]

if __name__=='__main__':
    caller()






