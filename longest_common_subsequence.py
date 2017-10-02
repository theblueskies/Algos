def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs

# print lcs('AGGTAB', 'GXTXAYB')


def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return ''
    elif X[m-1] == Y[n-1]:
        return X[m-1] + lcs_recursive(X, Y, m-1, n-1)
    else:
        result1 = lcs_recursive(X, Y, m, n-1)
        result2 = lcs_recursive(X, Y, m-1, n)

        final_result = result1 if len(result1) > len(result2) else result2
        return final_result

X = "apple"
Y = "bapplere"
print ("Length of LCS is ", lcs_recursive(X , Y, len(X), len(Y))[::-1])
