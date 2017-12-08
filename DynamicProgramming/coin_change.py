import sys

def getWays(n, c):
    # Complete this function
    number_of_ways = 0
    return _get_ways(n, c, number_of_ways)

def get_array_heuristic_value(array):
    tmp = 0
    for i in range(1,len(array)+1, 1):
        tmp += array[i-1]*i
    return tmp


def _get_ways(n, c, number_of_ways, path=[], total_path=[], add_set=set()):
    # import pdb; pdb.set_trace()
    if n == 0:
      return path
    for coin in c:
      if coin<=n:
          copy_of_path = path[:]
          path.append(coin)
          new_path = _get_ways(n-coin, c, number_of_ways, path, total_path)
        #   import pdb; pdb.set_trace()
          sorted_path = path
          heuristic = get_array_heuristic_value(sorted_path)
          if heuristic not in add_set:
              total_path.append(sorted_path)
            #   import pdb; pdb.set_trace()
              add_set.add(heuristic)
          path = copy_of_path[:]

    return total_path


# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(4, [1,2,3])
print(ways)
