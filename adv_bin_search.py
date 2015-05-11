def binarySearchAdvanced(array, target, low, high):
    #check = binarySearch(array,target,low,high)
    left_index=0
    right_index=0
    if high<low:
        return -1
    mid=(low+high)/2
    if array[mid] == target:
        if array[mid-1]<target:
            return mid
        left_index =  binarySearchAdvanced(array,target,low,mid)
    mid=(high+low)/2
    if array[mid] == target:
        if array[mid+1]>target:
            return mid
        right_index = binarySearchAdvanced(array,target,mid,high)
    return(left_index,right_index)

sample = [1,1,1,2,3,3,3,3,4,4,4,4,5,6,6,8,8,8,8,9]
print binarySearchAdvanced(sample, 3, 0, len(sample)-1)
