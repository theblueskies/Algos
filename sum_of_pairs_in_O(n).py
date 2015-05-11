
def sum_of_all_pairs():

    arr = [1,2,3]
    arr_single_sum=0
    all_pairs = 0

    for x in range(len(arr)):
        arr_single_sum+=arr[x]
    print "single sum =", arr_single_sum

    for x in range(len(arr)):
        all_pairs += arr_single_sum + arr[x]*(len(arr)-2)

    return all_pairs

print(sum_of_all_pairs())