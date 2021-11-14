def matrix_bool_add(a,b):#Return a list with 2 demensions.
    sum_result=[(a[i][j]+b[i][j])%2 for i in range(len(a)) for j in range(len(b[0])) ]
    pack=[sum_result[x:x+len(a[0])] for x in range(0,len(sum_result),len(a[0]))]
    return pack