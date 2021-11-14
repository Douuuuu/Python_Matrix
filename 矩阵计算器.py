def matrix_input():#Retrun a list with 2 demensions.
    nm_str=input("请输入行数和列数并以空格分隔,按回车结束\n")
    n=int(nm_str.split(' ')[0])
    m=int(nm_str.split(' ')[1])
    numbers_str=input("请输入数据并以空格分隔,按回车结束\n")
    numbers=[]
    for i in range(n*m):
        numbers.append(int(numbers_str.split(' ')[i]))
    pack=[numbers[x:x+m] for x in range(0,n*m,m)]
    return pack
def matrix_bool_input():#Retrun a list with 2 demensions. 
    nm_str=input("请输入行数和列数并以空格分隔，按回车结束\n")
    n=int(nm_str.split(' ')[0])
    m=int(nm_str.split(' ')[1])
    numbers_str=input("请输入数据,无分隔,按回车结束\n")
    numbers=[]
    for i in range(n*m):
        numbers.append(int(numbers_str[i]))
    pack=[numbers[x:x+m] for x in range(0,n*m,m)]
    return pack
def matrix_common_add(a,b):#Return a list with 2 demensions.
    sum_result=[a[i][j]+b[i][j] for i in range(len(a)) for j in range(len(b[0])) ]
    pack=[sum_result[x:x+len(a[0])] for x in range(0,len(sum_result),len(a[0]))]
    return pack
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
def matrix_bool_xor(a,b):#Return a list with 2 demensions.
    sum_result=[(a[i][j]+b[i][j])%2 for i in range(len(a)) for j in range(len(b[0])) ]
    pack=[sum_result[x:x+len(a[0])] for x in range(0,len(sum_result),len(a[0]))]
    return pack
def matrix_bool_multiply(a,b):#Retrun a list with 2 demensions. 
    if len(a[0])!=len(b):
        print("Can't run this alogrithm")
        return 0
    by_result=[0 for i in range(len(a)) for j in range(len(b[0]))]
    pack=[by_result[x:x+len(b[0])] for x in range(0,len(a)*len(b[0]),len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum+=a[i][k]*b[k][j]
            if   sum!=0:
                pack[i][j]=1
    return pack
def matrix_harmin_multiply(a,b):#Retrun a list with 2 demensions. 
    if len(a[0])!=len(b):
        print("Can't run this alogrithm")
        return 0
    by_result=[0 for i in range(len(a)) for j in range(len(b[0]))]
    pack=[by_result[x:x+len(b[0])] for x in range(0,len(a)*len(b[0]),len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum+=a[i][k]*b[k][j]
            pack[i][j]=sum%2
    return pack
def input_order():
    order=input("请输入需要的计算类型:")
    if order in ["求和", "求布尔异或" ,"求积", "求布尔积", "求布尔汉铭距离"]:
        return order
    else:
        print("无所输入的计算类型，请重新输入")
        return input_order()
def input_left_or_right():
    left_or_right=input("现有的矩阵为左或右，请输入 左 或 右:")
    if left_or_right in ["左","右"]:
        return left_or_right
    else:
        print("输入有误，请重新输入")
        return input_left_or_right()
def input_save_or_not():
    save_or_not=input("请输入是否保留结果，请输入 是 或 否:")
    if save_or_not in ["是","否"]:
        return save_or_not
    else:
        print("输入有误，请重新输入")
        return input_save_or_not()
def compute(matrix_ini_=[[]]):
    print("\n\n")
    matrix1=[[]]
    matrix2=[[]]
    matrix_result=[[]]
    order=input_order()
    if matrix_ini_!=[[]]:
        left_or_right=input_left_or_right()
        if left_or_right=="左":
            matrix1=matrix_ini_
        if left_or_right=="右":
            matrix2=matrix_ini_
    if order in ["求和","求积"] and matrix_ini_==[[]]:
        matrix1=matrix_input()
        matrix2=matrix_input()
        if order=="求和":
            matrix_result=matrix_common_add(matrix1,matrix2)
        if order=="求积":
            matrix_result=matrix_common_multiply(matrix1,matrix2)
    if order in ["求和","求积"] and matrix_ini_!=[[]]:
        if left_or_right=="左":
            matrix2=matrix_input()
        if left_or_right=="右":
            matrix1=matrix_input()
        if order=="求和":
            matrix_result=matrix_common_add(matrix1,matrix2)
        if order=="求积":
            matrix_result=matrix_common_multiply(matrix1,matrix2)
    if order in ["求布尔异或","求布尔积","求布尔汉铭距离"] and matrix_ini_==[[]]:
        matrix1=matrix_bool_input()
        matrix2=matrix_bool_input()
        if order=="求布尔异或":
            matrix_result=matrix_bool_xor(matrix1,matrix2)
        if order=="求布尔积":
            matrix_result=matrix_bool_multiply(matrix1,matrix2)
        if order=="求布尔汉铭距离":
            matrix_result=matrix_harmin_multiply(matrix1,matrix2)
    if order in ["求布尔异或","求布尔积","求布尔汉铭距离"] and matrix_ini_!=[[]]:
        if left_or_right=="左":
            matrix1=matrix_ini_
            matrix2=matrix_bool_input()
        if left_or_right=="右":
            matrix1=matrix_bool_input()
            matrix2=matrix_ini_
        if order=="求布尔异或":
            matrix_result=matrix_bool_xor(matrix1,matrix2)
        if order=="求布尔积":
            matrix_result=matrix_bool_multiply(matrix1,matrix2)
        if order=="求布尔汉铭距离":
            matrix_result=matrix_harmin_multiply(matrix1,matrix2)
    print("计算结果为:")
    print(matrix_result)
    save_or_not=input_save_or_not()
    if save_or_not=="是":
        print("保留的矩阵是:")
        for i in range(len(matrix_result)):
            print(matrix_result[i])
        compute(matrix_result)
    if save_or_not=="否":
        compute()
    
def begin():
    print("计算类型:求和 求布尔异或 求积 求布尔积 求布尔汉铭距离\n")
    compute()

begin()
            

    


