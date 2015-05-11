def missing_num():
    arr = [1,3,5,9]
    summation=0
    for x in arr:
        summation+=x
    act_sum = int(.5*(len(arr)+1)*(arr[0]+arr[len(arr)-1]))
    diff = act_sum-summation

    print diff



missing_num()