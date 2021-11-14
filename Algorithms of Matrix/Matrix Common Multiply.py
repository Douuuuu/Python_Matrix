def matrix_common_multiply(a,b):#Retrun a list with 2 demensions. 
    if len(a[0])!=len(b):
        print("Can't run this alogrithm,because the col of the first matrix is not same as the row of the second matrix")
        return 0
    by_result=[0 for i in range(len(a)) for j in range(len(b[0]))]
    pack=[by_result[x:x+len(b[0])] for x in range(0,len(a)*len(b[0]),len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum+=a[i][k]*b[k][j]
            pack[i][j]=sum
    return pack