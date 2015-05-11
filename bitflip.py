
def  bitFlip( arr):
    count = number_of_ones(arr)
    for left in range(len(arr)):
        for right in range(left, len(arr), 1):
            new_arr=arr[:]
            new_arr = subflip(left, right, new_arr)
            new_count = number_of_ones(new_arr)
            if new_count>count:
                count = new_count
    return count




def subflip(left, right, change_arr):
    change_arr = change_arr
    for x in range(left,right,1):
        if change_arr[x]==1:
            change_arr[x]=0
        else:
            change_arr[x]=1
    return change_arr

def number_of_ones(change_arr):
    count = 0
    for x in change_arr:
        if x==1:
            count+=1
    return count

arr = [1,0,0,1,0,0,1,0]
res= bitFlip(arr)
print res
